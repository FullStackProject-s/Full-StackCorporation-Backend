from .base_message_perms import (
    BaseMessagePerms
)
from organization.models import Organization


class IsAdministratorOrOwnerOrReadOnlyReassignment(
    BaseMessagePerms
):
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True

        return bool(
            Organization.objects.filter(
                owner=user
            ).exists() or
            Organization.objects.filter(
                members__username=user.username
            ).exists()
        )

    def has_object_permission(self, request, view, obj):
        if not obj.is_active:
            return False
        return super().has_object_permission(
            request,
            view,
            obj.organization
        )
