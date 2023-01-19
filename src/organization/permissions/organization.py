from user.permissions import IsOwnerOrReadOnlyCustomUser

from employee.models import Administrator


class IsAdministratorOrOwnerOrReadOnlyOrganization(
    IsOwnerOrReadOnlyCustomUser
):
    def has_object_permission(self, request, view, obj):
        if super().has_object_permission(request, view, obj.owner):
            return True
        admin = Administrator.objects.filter(profile__user=request.user)

        if not admin.exists():
            return False

        if admin.first().profile.user in obj.members.all():
            return True

        return False
