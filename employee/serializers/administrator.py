from rest_framework import serializers

from employee.models import Administrator
from employee.serializers.baseSerializers import BaseStaffSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin
)

from user.models.consts import StaffRole


class AdministratorSerializer(
    BaseStaffSerializer,
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin

):
    class Meta:
        model = Administrator
        fields = (
            *BaseStaffSerializer.Meta.fields,
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.ADMIN
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)

