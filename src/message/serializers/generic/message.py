from rest_framework import serializers

from message.models import (
    Reassignment,
    Task,
    CompletedTasks
)


class BaseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'pk',
            'creator',
            'text',
            'create_at',
        )


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


class BaseTaskSerializer(BaseMessageSerializer):
    class Meta(BaseMessageSerializer.Meta):
        model = Task


class BaseCompletedTasksSerializer(BaseMessageSerializer):
    checked = serializers.BooleanField(read_only=True)

    class Meta(BaseMessageSerializer.Meta):
        model = CompletedTasks
        fields = (
            *BaseMessageSerializer.Meta.fields,
            'tasks',
            'checked',
        )
