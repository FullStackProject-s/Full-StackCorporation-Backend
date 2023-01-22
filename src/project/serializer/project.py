from rest_framework import serializers

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from project.serializer.generics import BaseProjectSerializer


class ProjectShowSerializer(BaseProjectSerializer):
    deadline = serializers.DateField()
    organization = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_organization(self, obj):
        if obj.organization:
            return obj.organization.organization_name
        return None


class ProjectSerializer(BaseProjectSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)

        organization = validated_data.get('organization')
        organization.projects.add(instance)
        organization.save()

        return instance

    def to_representation(self, instance):
        return ProjectShowSerializer(instance).data
