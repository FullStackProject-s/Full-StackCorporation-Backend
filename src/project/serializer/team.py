from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)

from project.serializer.services import _update_personal, _create_personal
from project.serializer.generics import BaseTeamSerializer


class TeamShowSerializer(BaseTeamSerializer):
    team_lead = DeveloperShowSerializer()
    project_manager = ProjectManagerShowSerializer()
    developers = DeveloperShowSerializer(many=True)


class TeamSerializer(BaseTeamSerializer):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)
        _create_personal(instance)
        return instance

    def update(self, instance, validated_data):
        _update_personal(instance, validated_data)
        return super().update(instance, validated_data)
