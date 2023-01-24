from rest_framework import permissions

from organization.permissions import (
    IsAdministratorOrOwnerOrReadOnlyOrganization
)


class BaseMessagePerms(IsAdministratorOrOwnerOrReadOnlyOrganization, ):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return super().has_object_permission(request, view, obj)


class IsOwnerOrSuperUserMessagePerms(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.creator == request.user:
            return True
        return False
