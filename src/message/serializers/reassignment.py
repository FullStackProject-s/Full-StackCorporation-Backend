from rest_framework import serializers

from message.serializers.generic import BaseMessageSerializer
from message.models import Reassignment

from project.serializer import ProjectShowSerializer, TeamShowSerializer


class BaseReassignmentSerializer(BaseMessageSerializer):
    confirmed = serializers.BooleanField(read_only=True)

    class Meta:
        model = Reassignment
        fields = (
            *BaseMessageSerializer.Meta.fields,
            'from_project',
            'to_project',
            'from_team',
            'to_team',
            'confirmed',
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
