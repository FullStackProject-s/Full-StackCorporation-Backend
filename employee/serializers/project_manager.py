from employee.models import ProjectManager
from employee.serializers.generics import BaseProjectManagerSerializer

from user.serializers import ProfileShowSerializer


class ProjectManagerShowSerializer(BaseProjectManagerSerializer):
    profile = ProfileShowSerializer(required=False, read_only=True)


class ProjectManagerSerializer(BaseProjectManagerSerializer):
    def to_representation(self, instance):
        return ProjectManagerShowSerializer(instance).data
