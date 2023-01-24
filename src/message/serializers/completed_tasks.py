from rest_framework import serializers

from message.serializers.generic import BaseCompletedTasksSerializer
from user.serializers import CustomUserShowSerializer

from .task import TaskShowSerializer


class CompletedTasksShowSerializer(BaseCompletedTasksSerializer):
    creator = CustomUserShowSerializer(read_only=True)
    tasks = TaskShowSerializer(many=True, read_only=True)


class CompletedTasksSerializer(BaseCompletedTasksSerializer):

    def to_representation(self, instance):
        return CompletedTasksShowSerializer(instance).data

    class Meta(BaseCompletedTasksSerializer.Meta):
        extra_kwargs = {
            **BaseCompletedTasksSerializer.Meta.extra_kwargs,
            'organization': {'read_only': False, 'required': True}
        }


class CompletedTasksUpdateSerializer(CompletedTasksShowSerializer):
    checked = serializers.BooleanField(read_only=False)

    class Meta(BaseCompletedTasksSerializer.Meta):
        pass
