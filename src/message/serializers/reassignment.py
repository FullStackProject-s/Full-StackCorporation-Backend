from rest_framework import serializers

from message.serializers.generic import BaseReassignmentSerializer

from user.serializers import CustomUserShowSerializer


class ReassignmentShowSerializer(BaseReassignmentSerializer):
    creator = CustomUserShowSerializer(read_only=True)


class ReassignmentSerializer(BaseReassignmentSerializer):
    def to_representation(self, instance):
        return ReassignmentShowSerializer(instance).data

    class Meta(BaseReassignmentSerializer.Meta):
        extra_kwargs = {
            **BaseReassignmentSerializer.Meta.extra_kwargs,
            'organization': {'read_only': False, 'required': True}
        }


class ReassignmentUpdateSerializer(ReassignmentShowSerializer):
    confirmed = serializers.BooleanField(read_only=False)
