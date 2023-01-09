from rest_framework import serializers

from project.serializer import TeamSerializer

from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    teams = TeamSerializer(many=True, read_only=True)
    deadline = serializers.DateField()
    create_at = serializers.DateField(read_only=True)

    class Meta:
        model = Project
        fields = (
            'pk',
            'project_name',
            'teams',
            'organization',
            'create_at',
            'deadline'

        )
