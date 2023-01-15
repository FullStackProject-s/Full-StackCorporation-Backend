from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from employee.serializers import DeveloperSerializer

from employee.serializers.generics import BaseDeveloperOrgSpecialtySerializer


class DeveloperOrgSpecialtyShowSerializer(BaseDeveloperOrgSpecialtySerializer):
    organization_developer = DeveloperSerializer(read_only=True)
    organization = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_organization(self, obj):
        if obj.organization:
            return obj.organization.organization_name
        return None


class DeveloperOrgSpecialtySerializer(BaseDeveloperOrgSpecialtySerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.organization_developer.append_specialties(instance)
        return instance

    def to_representation(self, instance):
        return DeveloperOrgSpecialtyShowSerializer(instance).data


class DeveloperOrgSpecialtyUpdateSerializer(DeveloperOrgSpecialtySerializer):
    class Meta(DeveloperOrgSpecialtySerializer.Meta):
        fields = (
            'specialty',
        )
