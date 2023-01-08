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
    specialties = serializers.SerializerMethodField()

    class Meta(BaseManagerDeveloperSerializer.Meta):
        model = Developer
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
            'skill_level',
            'specialties',
            'stack',
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.DEVELOPER,
        )

    def get_specialties(self, obj: Developer):
        if obj.specialties:
            return [
                specialty.specialty
                for specialty in obj.specialties.all()
            ]
        return None


class DeveloperStackTechnologiesSerializer(serializers.Serializer):
    technology_names = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        fields = (
            'technology_names',
        )
