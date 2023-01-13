from rest_framework import serializers

from message.serializers.generic import BaseReassignmentSerializer

from project.serializer import (
    ProjectShowSerializer,
    TeamShowSerializer
)

class ReassignmentShowSerializer(BaseReassignmentSerializer):
    from_project = ProjectShowSerializer(read_only=True)
    to_project = ProjectShowSerializer(read_only=True)
    from_team = TeamShowSerializer(read_only=True)
    to_team = TeamShowSerializer(read_only=True)


class ReassignmentSerializer(BaseReassignmentSerializer):
    def to_representation(self, instance):
        return ReassignmentShowSerializer(instance).data


class ReassignmentUpdateSerializer(ReassignmentSerializer):
    confirmed = serializers.BooleanField(read_only=False)
