from rest_framework import serializers
from employee.models.employees import ProjectManager
from user.serializers.profile import ProfileSerializer


class ProjectManagerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = ProjectManager
        fields = (
            'profile',
        )
