from rest_framework import serializers

from message.serializers.generic import BaseCompletedTasksSerializer

from .task import TaskShowSerializer


class CompletedTasksShowSerializer(BaseCompletedTasksSerializer):
    tasks = TaskShowSerializer(many=True, read_only=True)


class CompletedTasksSerializer(BaseCompletedTasksSerializer):
    def to_representation(self, instance):
        return CompletedTasksShowSerializer(instance).data


class CompletedTasksUpdateSerializer(CompletedTasksSerializer):
    checked = serializers.BooleanField(read_only=False)
