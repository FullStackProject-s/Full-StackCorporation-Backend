from organization.permissions import (
    IsAdministratorOrOwnerOrReadOnlyOrganization
)


class IsAdministratorOrOwnerOrReadOnlyProject(
    IsAdministratorOrOwnerOrReadOnlyOrganization
):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return super().has_object_permission(request, view, obj.organization)
