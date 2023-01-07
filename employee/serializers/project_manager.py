from employee.models import ProjectManager
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin
)

from user.models.consts import StaffRole


class ProjectManagerSerializer(
    BaseManagerDeveloperSerializer,
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin
):
    class Meta:
        model = ProjectManager
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.PRODUCT_MANAGER,
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
