from .base_message_perms import (
    BaseMessagePerms
)
from organization.models import Organization

from employee.models import Administrator


class IsAdministratorOrOwnerOrReadOnlyTask(
    BaseMessagePerms
):
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        if Organization.objects.filter(owner=user):
            return True

        admin = Administrator.objects.filter(profile__user=user)

        if not admin.exists():
            return False
        if Organization.objects.filter(
                members__profile__administrator=admin.first()
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if not obj.is_active:
            return False
        return super().has_object_permission(
            request,
            view,
            obj.organization
        )
