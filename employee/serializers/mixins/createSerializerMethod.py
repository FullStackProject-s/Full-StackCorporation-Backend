from django.db import transaction

from employee.models import Developer
from employee.serializers.services import SetUserPermission
from user.models import Permissions


class StaffCreateSerializerMixin:
    def _staff_create(self, validated_data, role_name, **kwargs):
        with transaction.atomic():
            _profile = self._create_profile(validated_data.pop('profile'))

            obj = self.Meta.model.objects.create(
                **validated_data,
                profile=_profile,
                **kwargs
            )
            permission, created_ = Permissions.objects.get_or_create(
                role_name=f'{role_name}'
            )
            SetUserPermission.set_permissions(
                obj.profile.user.username,
                permission
            )
            obj.profile.user.staff_role = permission
            return obj
