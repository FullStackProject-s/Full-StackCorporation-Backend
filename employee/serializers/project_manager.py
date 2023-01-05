from employee.models import ProjectManager
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)

from user.models.consts import StaffRole
from user.serializers.mixins import CreateCustomUserSerializerMixin


class ProjectManagerSerializer(
    BaseManagerDeveloperSerializer,
    ProfileUpdateSerializerMixin,
    CreateCustomUserSerializerMixin,
    StaffCreateSerializerMixin
):
    class Meta:
        model = ProjectManager
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
        )

    def create(self, validated_data):
        return self._staff_create(
            validated_data,
            StaffRole.PRODUCT_MANAGER
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
