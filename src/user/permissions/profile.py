from user.permissions.user import IsOwnerOrReadOnlyCustomUser


class IsOwnerOrReadOnlyProfile(IsOwnerOrReadOnlyCustomUser):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(
            request,
            view,
            obj.user
        )
