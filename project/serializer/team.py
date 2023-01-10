from rest_framework import serializers
from project.models.team import Team
from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)
from project.serializer.mixins import UpdateTeamMixin


class BaseTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'pk',
            'team_name',
            'team_lead',
            'project_manager',
            'developers',
            'create_at'
        )


class TeamShowSerializer(BaseTeamSerializer):
    team_lead = DeveloperShowSerializer()
    project_manager = ProjectManagerShowSerializer()
    developers = DeveloperShowSerializer(many=True)


class TeamSerializer(
    BaseTeamSerializer,
    UpdateTeamMixin
):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data

    def update(self, instance, validated_data):
        self._update(instance, validated_data)
        return super().update(instance, validated_data)
