from django.db import transaction
from rest_framework import serializers

from employee.serializers.services import SetUserPermission
from user.models import Permissions, Profile


class StaffPermissionsSetSerializerMixin:
    def _set_permissions(self, obj, role_name):
        with transaction.atomic():
            permission, created_ = Permissions.objects.get_or_create(
                role_name=f'{role_name}'
            )
            SetUserPermission.set_permissions(
                obj.profile.user.username,
                permission
            )
            obj.profile.user.staff_role = permission
            return obj
