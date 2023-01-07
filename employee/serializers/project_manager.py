from employee.models import ProjectManager
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)

from user.models.consts import StaffRole


class ProjectManagerSerializer(
    BaseManagerDeveloperSerializer,
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
):
    class Meta:
        model = ProjectManager
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
        )

    def create(self, validated_data):
        specialty = validated_data.pop('get_specialty_display')
        return self._staff_create(
            validated_data,
            StaffRole.PRODUCT_MANAGER,
            specialty=specialty
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
