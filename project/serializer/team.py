from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)

from project.serializer.services import _update_personal
from project.serializer.generics import BaseTeamSerializer


class TeamShowSerializer(BaseTeamSerializer):
    team_lead = DeveloperShowSerializer()
    project_manager = ProjectManagerShowSerializer()
    developers = DeveloperShowSerializer(many=True)


class TeamSerializer(BaseTeamSerializer):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data

    def update(self, instance, validated_data):
        _update_personal(instance, validated_data)
        return super().update(instance, validated_data)
