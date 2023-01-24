from message.serializers.generic import BaseTaskSerializer

from user.serializers import CustomUserShowSerializer
from rest_framework import serializers


class TaskShowSerializer(BaseTaskSerializer):
    creator = CustomUserShowSerializer(read_only=True)


class TaskSerializer(BaseTaskSerializer):
    def to_representation(self, instance):
        return TaskShowSerializer(instance).data

    class Meta(BaseTaskSerializer.Meta):
        extra_kwargs = {
            **BaseTaskSerializer.Meta.extra_kwargs,
            'organization': {'read_only': False, 'required': True}
        }


class TaskUpdateSerializer(TaskShowSerializer):
    completed = serializers.BooleanField(read_only=False)
