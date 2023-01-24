from .base_message_perms import (
    BaseMessagePerms
)


class IsAdministratorOrOwnerOrReadOnlyInvite(
    BaseMessagePerms
):
    def has_object_permission(self, request, view, obj):
        if not obj.is_active:
            return False
        return super().has_object_permission(
            request,
            view,
            obj.to_organization
        )
