from rest_framework import serializers
from project.models.team import Team
from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)


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


class TeamSerializer(BaseTeamSerializer):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'team_name',
        )


class TeamTeamLeadSerializer(serializers.Serializer):
    team_lead = serializers.CharField()

    class Meta:
        fields = (
            'team_lead'
        )


class TeamProjectManagerSerializer(serializers.Serializer):
    project_manager = serializers.CharField()

    class Meta:
        fields = (
            'project_manager'
        )


class TeamDevelopersSerializer(serializers.Serializer):
    developers = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        fields = (
            'developers',
        )
