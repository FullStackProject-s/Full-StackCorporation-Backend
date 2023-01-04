from rest_framework import serializers
from project.models.team import Team
from employee.serializers.developer import DeveloperSerializer
from employee.serializers.project_manager import ProjectManagerSerializer


class TeamSerializer(serializers.ModelSerializer):
    team_lead = DeveloperSerializer()
    project_manager = ProjectManagerSerializer()
    developers = DeveloperSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'team_name',
            'team_lead',
            'project_manager',
            'developers',
        )
