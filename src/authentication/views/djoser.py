from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils.timezone import now
from djoser import signals
from djoser.compat import get_user_email  # noqa
from djoser.views import UserViewSet

from authentication.tasks import (
    send_reset_password_email,
    send_activation_user_email,
    send_reset_password_confirmation_email
)


class CustomUserViewSet(UserViewSet):
    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )
        send_activation_user_email.delay(
            {
                'user_id': user.id,
            },
            [get_user_email(user)]

        )

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()

        if user:
            send_reset_password_email.delay(
                {
                    'user_id': user.id,
                },
                [get_user_email(user)]
            )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def reset_password_confirm(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.user.set_password(serializer.data["new_password"])
        if hasattr(serializer.user, "last_login"):
            serializer.user.last_login = now()
        serializer.user.save()

        send_reset_password_confirmation_email.delay(
            {
                'user_id': serializer.user.id,
            },
            [get_user_email(serializer.user)]
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
