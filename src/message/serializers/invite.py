from message.serializers.generic import BaseInviteToOrganizationSerializer


class InviteToOrganizationShowSerializer(
    BaseInviteToOrganizationSerializer
):
    pass


class InviteToOrganizationSerializer(
    BaseInviteToOrganizationSerializer
):
    def to_representation(self, instance):
        return InviteToOrganizationShowSerializer(instance).data


class InviteToOrganizationUpdateSerializer(
    BaseInviteToOrganizationSerializer
):
    class Meta(BaseInviteToOrganizationSerializer.Meta):
        extra_kwargs = {
            **BaseInviteToOrganizationSerializer.Meta.extra_kwargs,
            'status': {'read_only': False},
            'to_organization': {'read_only': True},
            'creator': {'read_only': True}
        }
