from message.serializers.generic import BaseTaskSerializer

from user.serializers import CustomUserShowSerializer


class TaskShowSerializer(BaseTaskSerializer):
    creator = CustomUserShowSerializer(read_only=True)

    class Meta(BaseTaskSerializer.Meta):
        fields = (
            *BaseTaskSerializer.Meta.fields,
            'completed',
        )


class TaskSerializer(BaseTaskSerializer):
    def to_representation(self, instance):
        return TaskShowSerializer(instance).data


class TaskUpdateSerializer(TaskShowSerializer):
    pass
