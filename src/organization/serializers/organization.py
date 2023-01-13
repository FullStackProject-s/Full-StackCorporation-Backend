from organization.serializers.services import (
    _update_projects,
    _create_projects
)
from user.serializers.user import CustomUserShowSerializer
from organization.serializers.generic import BaseOrganizationSerializer
from project.serializer import ProjectShowSerializer


class OrganizationShowSerializer(BaseOrganizationSerializer):
    owner = CustomUserShowSerializer(read_only=True)
    projects = ProjectShowSerializer(many=True, read_only=True)
    members = CustomUserShowSerializer(many=True, read_only=True)


class OrganizationSerializer(BaseOrganizationSerializer):
    def to_representation(self, instance):
        return OrganizationShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)
        _create_projects(instance)
        return instance

    def update(self, instance, validated_data):
        _update_projects(instance, validated_data)
        return super().update(instance, validated_data)
