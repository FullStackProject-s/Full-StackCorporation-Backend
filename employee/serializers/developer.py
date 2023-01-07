from rest_framework import serializers

from employee.models.employees import Developer
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.technologies import TechnologiesSerializer
from employee.serializers.mixins import StaffPermissionsSetSerializerMixin

from user.models.consts import StaffRole


class DeveloperSerializer(
    BaseManagerDeveloperSerializer,
    StaffPermissionsSetSerializerMixin
):
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )

    class Meta(BaseManagerDeveloperSerializer.Meta):
        model = Developer
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
            'specialty',
            'skill_level',
            'stack',
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.DEVELOPER,
        )

class DeveloperStackTechnologiesSerializer(serializers.Serializer):
    technology_names = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        fields = (
            'technology_names',
        )
