from rest_framework import serializers

from message.models import (
    Reassignment,
    Task,
    CompletedTasks,
    InviteToOrganization
)


class BaseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = (
            'pk',
            'creator',
            'text',
            'is_active',
            'create_at',
        )
        extra_kwargs = {'is_active': {'read_only': True}}


class BaseInviteToOrganizationSerializer(BaseMessageSerializer):
    class Meta(BaseMessageSerializer.Meta):
        model = InviteToOrganization
        fields = (
            *BaseMessageSerializer.Meta.fields,
            'to_organization',
            'status'
        )
        extra_kwargs = {
            **BaseMessageSerializer.Meta.extra_kwargs,
            'status': {'read_only': True}
        }


class BaseOrganizationSerializer(BaseMessageSerializer):
    class Meta(BaseMessageSerializer.Meta):
        fields = (
            *BaseMessageSerializer.Meta.fields,
            'organization'
        )
        extra_kwargs = {
            **BaseMessageSerializer.Meta.extra_kwargs,
            'organization': {'read_only': True}
        }


class BaseReassignmentSerializer(BaseOrganizationSerializer):
    confirmed = serializers.BooleanField(read_only=True)

    class Meta(BaseOrganizationSerializer.Meta):
        model = Reassignment
        fields = (
            *BaseOrganizationSerializer.Meta.fields,
            'from_project',
            'to_project',
            'from_team',
            'to_team',
            'confirmed',
        )


class BaseTaskSerializer(BaseOrganizationSerializer):
    completed = serializers.BooleanField(read_only=True)

    class Meta(BaseOrganizationSerializer.Meta):
        model = Task
        fields = (
            *BaseOrganizationSerializer.Meta.fields,
            'completed'
        )


class BaseCompletedTasksSerializer(BaseOrganizationSerializer):
    checked = serializers.BooleanField(read_only=True)

    class Meta(BaseOrganizationSerializer.Meta):
        model = CompletedTasks
        fields = (
            *BaseOrganizationSerializer.Meta.fields,
            'tasks',
            'checked',
        )
