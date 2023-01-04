from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from user.models.profile import Profile
from user.serializers.mixins.create_custom_user import \
    CreateCustomUserSerializerMixin
from user.serializers.user import CustomUserSerializer


class ProfileSerializer(
    serializers.ModelSerializer,
    CreateCustomUserSerializerMixin
):
    user = CustomUserSerializer()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'pk',

            'user',
            'photo_url',
            'about_user'
        )

    @extend_schema_field(OpenApiTypes.URI)
    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.avatar:
            photo_url = obj.avatar.url
            return request.build_absolute_uri(photo_url)
        return 'unknown/'

    def create(self, validated_data):
        return self._create_profile(validated_data)

    def update(self, instance, validated_data):
        _user_data = validated_data.pop('user', None)
        user_serializer = self.fields['user']
        if _user_data:
            user_serializer.update(instance.user, _user_data)
        return super().update(instance, validated_data)
