from rest_framework import serializers

from project.serializer import TeamSerializer

from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)
    create_at = serializers.DateField(read_only=True)

    class Meta:
        model = Project
        fields = (
            'name',
            'teams',
            'create_at',
            'deadline'

        )
