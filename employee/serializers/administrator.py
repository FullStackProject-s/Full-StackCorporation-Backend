from employee.models import Administrator
from employee.serializers.baseSerializers import BaseStaffSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)

from user.models.consts import StaffRole
from user.serializers.mixins import CreateCustomUserSerializerMixin


class AdministratorSerializer(
    BaseStaffSerializer,
    CreateCustomUserSerializerMixin,
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
):
    class Meta:
        model = Administrator
        fields = (
            *BaseStaffSerializer.Meta.fields,
        )

    def create(self, validated_data):
        return self._staff_create(
            validated_data,
            StaffRole.ADMIN
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
