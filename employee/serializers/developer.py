from drf_spectacular.plumbing import build_array_type, build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from rest_framework import serializers

from employee.models.employees import Developer
from employee.serializers.generics import BaseManagerDeveloperSerializer
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

    @extend_schema_field(build_array_type(build_basic_type(OpenApiTypes.STR)))
    def get_specialties(self, obj: Developer):
        if obj.specialties:
            return [
                f'{specialty.specialty} - ' \
                f'{specialty.organization.organization_name}'
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
