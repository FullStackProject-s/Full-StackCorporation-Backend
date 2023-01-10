from rest_framework import serializers

from drf_spectacular.plumbing import build_array_type, build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from employee.serializers.generics import BaseDeveloperSerializer
from employee.serializers.technologies import TechnologiesSerializer

from user.serializers import ProfileShowSerializer


class DeveloperShowSerializer(BaseDeveloperSerializer):
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )
    specialties = serializers.SerializerMethodField()
    profile = ProfileShowSerializer(read_only=True)

    @extend_schema_field(build_array_type(build_basic_type(OpenApiTypes.STR)))
    def get_specialties(self, obj):
        if obj.specialties:
            return [
                f'{specialty.specialty} - ' \
                f'{specialty.organization.organization_name}'
                for specialty in obj.specialties.all()
            ]
        return None


class DeveloperSerializer(BaseDeveloperSerializer):
    def to_representation(self, instance):
        return DeveloperShowSerializer(instance).data
