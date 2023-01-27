from django.utils.timezone import now

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from djoser import signals
from djoser.compat import get_user_email  # noqa
from djoser.views import UserViewSet

from authentication.tasks import (
    send_reset_password_email,
    send_activation_user_email,
    send_activation_confirmation_user_email,
    send_reset_password_confirmation_email
)

from authentication.views import logger


class CustomUserViewSet(UserViewSet):
    """
    Overridden djoser UserViewSet for integration celery task sending email.
    """

    def perform_create(self, serializer):
        """
        Create :model:`user.CustomUser`.
        Sending activation email after created.
        """

        user = serializer.save()

        logger.info(
            f'User created, pk: `{user.pk}`, username: `{user.username}`'
        )

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
    def activation(self, request, *args, **kwargs):
        """
        Endpoint for activate user by uid and token,
        which get by email message.
        After user activation send confirmation email.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        user.is_active = True
        user.save()

        logger.info(
            f'User activate confirmation, pk: `{user.pk}`, '
            f'username: `{user.username}`'
        )

        send_activation_confirmation_user_email.delay(
            {
                'user_id': user.id,
            },
            [get_user_email(user)]
        )

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        """
        Sending reset password email, which includes uid and token to
        confirm password reset
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.get_user()

        logger.info(
            f'User reset password, pk: `{user.pk}`, '
            f'username: `{user.username}`'
        )

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
        """
        Confirm reset password email, take uid, token and new password.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.user.set_password(serializer.data["new_password"])
        if hasattr(serializer.user, "last_login"):
            serializer.user.last_login = now()
        serializer.user.save()

        logger.info(
            f'User reset password confirmation, pk: `{serializer.user.pk}`, '
            f'username: `{serializer.user.username}`'
        )

        send_reset_password_confirmation_email.delay(
            {
                'user_id': serializer.user.id,
            },
            [get_user_email(serializer.user)]
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
