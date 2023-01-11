from rest_framework import serializers

from user.models import Profile


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
