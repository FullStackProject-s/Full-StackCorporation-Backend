from rest_framework import serializers

from project.models import Team


class BaseTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'pk',
            'team_name',
            'project',
            'team_lead',
            'project_manager',
            'developers',
            'create_at'
        )
