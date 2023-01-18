from user.permissions import IsOwnerOrReadOnlyProfile


class IsOwnerOrReadOnlyEmployee(IsOwnerOrReadOnlyProfile):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(
            request,
            view,
            obj.profile
        )
