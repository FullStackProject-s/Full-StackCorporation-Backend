from rest_framework import serializers

from organization.serializers import OrganizationShowOthersSerializer
from project.serializer.generics import BaseProjectSerializer


class ProjectShowSerializer(BaseProjectSerializer):
    deadline = serializers.DateField()
    organization = OrganizationShowOthersSerializer()


class ProjectShowOthersSerializer(BaseProjectSerializer):
    class Meta(BaseProjectSerializer.Meta):
        fields = (
            'pk',
            'project_name'
        )


class ProjectSerializer(BaseProjectSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)

        organization = validated_data.get('organization')
        organization.projects.add(instance)
        organization.save()

        return instance

    def to_representation(self, instance):
        return ProjectShowSerializer(instance).data
