from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)

from project.serializer.services import (
    update_personal,
    create_personal
)
from project.serializer.generics import BaseTeamSerializer


class TeamShowSerializer(BaseTeamSerializer):
    team_lead = DeveloperShowSerializer()
    project_manager = ProjectManagerShowSerializer()

    @extend_schema_field(OpenApiTypes.STR)
    def get_project(self, obj):
        if obj.project:
            return obj.project.project_name
        return None


class TeamSerializer(BaseTeamSerializer):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)
        create_personal(instance)

        project = validated_data.get('project')
        project.teams.add(instance)
        project.save()

        return instance

    def update(self, instance, validated_data):
        update_personal(instance, validated_data)
        return super().update(instance, validated_data)
