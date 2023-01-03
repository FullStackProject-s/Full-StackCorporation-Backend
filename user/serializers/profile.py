from rest_framework import serializers

from user.models.profile import Profile
from user.serializers.user import CustomUserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'user',
            'photo_url',
            'about_user'
        )

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.avatar.url
        return request.build_absolute_uri(photo_url)

    def update(self, instance, validated_data):
        _user_data = validated_data.pop('user', None)
        profile_serializer = self.fields['user']
        if _user_data:
            profile_serializer.update(instance.user, _user_data)
        return super().update(instance, validated_data)
