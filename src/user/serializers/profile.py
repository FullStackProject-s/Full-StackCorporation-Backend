from user.serializers.user import CustomUserShowSerializer
from user.serializers.generic import BaseProfileSerializer


class ProfileShowSerializer(BaseProfileSerializer):
    user = CustomUserShowSerializer(required=False, read_only=True)


class ProfileSerializer(BaseProfileSerializer):
    def to_representation(self, instance):
        return ProfileShowSerializer(instance).data


class ProfileImageUploadSerializer(BaseProfileSerializer):
    class Meta:
        model = BaseProfileSerializer.Meta.model
        fields = (
            'profile_avatar',
        )
