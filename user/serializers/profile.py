from rest_framework import serializers

from user.models.profile import Profile
from user.serializers.user import CustomUserShowSerializer


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'pk',
            'user',
            'profile_avatar',
            'about_user'
        )
        extra_kwargs = {'profile_avatar': {'read_only': True}}


class ProfileShowSerializer(BaseProfileSerializer):
    user = CustomUserShowSerializer(required=False, read_only=True)


class ProfileSerializer(BaseProfileSerializer):
    def to_representation(self, instance):
        return ProfileShowSerializer(instance).data
