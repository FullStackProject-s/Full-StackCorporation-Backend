from project.permissions import (
    IsAdministratorOrOwnerOrReadOnlyProject
)


class IsProjectManagerOrAdministratorOrOwnerOrReadOnlyTeam(
    IsAdministratorOrOwnerOrReadOnlyProject
):

    def has_object_permission(self, request, view, obj):
        if obj.project_manager and \
                obj.project_manager.profile.user == request.user:
            return True

        return super().has_object_permission(request, view, obj.project)
