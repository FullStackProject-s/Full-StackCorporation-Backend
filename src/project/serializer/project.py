from rest_framework import serializers

from organization.serializers import OrganizationShowProjectsSerializer
from project.serializer.generics import BaseProjectSerializer
from project.serializer.services.add_organization_in_project import (
    add_organization_in_project
)


class ProjectShowSerializer(BaseProjectSerializer):
    deadline = serializers.DateField()
    organization = OrganizationShowProjectsSerializer()


class ProjectShowOthersSerializer(BaseProjectSerializer):
    class Meta(BaseProjectSerializer.Meta):
        fields = (
            'pk',
            'project_name'
        )


class ProjectSerializer(BaseProjectSerializer):
    def create(self, validated_data):
        return add_organization_in_project(
            super().create(validated_data),
            validated_data
        )

    def to_representation(self, instance):
        return ProjectShowSerializer(instance).data
