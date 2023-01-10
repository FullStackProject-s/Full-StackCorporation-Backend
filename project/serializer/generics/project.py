from rest_framework import serializers

from project.models import Project


class BaseProjectSerializer(serializers.ModelSerializer):
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
