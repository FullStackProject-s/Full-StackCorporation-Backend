from django.contrib.auth import get_user_model

from general.models.utils import set_image_on_imagefield
from user.models import Profile

from user.serializers.permission import PermissionSerializer
from user.serializers.generic import BaseCustomUserSerializer
from user.serializers.services import create_permissions

User = get_user_model()


class CustomUserShowSerializer(BaseCustomUserSerializer):
    staff_role = PermissionSerializer(
        required=False,
        read_only=True
    )


class CustomUserSerializer(BaseCustomUserSerializer):

    def create(self, validated_data):
        validated_data['staff_role'] = create_permissions(
            validated_data['staff_role']
        )
        instance = User.objects.create_user(**validated_data)

        profile_instance = Profile.objects.create(user=instance)
        set_image_on_imagefield(
            profile_instance.user.username,
            profile_instance.user.email,
            imagefield=profile_instance.profile_avatar,
        )

        return instance

    def to_representation(self, data):
        return CustomUserShowSerializer(data).data

    class Meta(BaseCustomUserSerializer.Meta):
        fields = (
            *BaseCustomUserSerializer.Meta.fields,
            'password',
        )


class CustomUserSerializerUpdate(CustomUserSerializer):
    def update(self, instance, validated_data):
        if 'staff_role' in validated_data:
            validated_data['staff_role'] = create_permissions(
                validated_data['staff_role']
            )

        return super().update(instance, validated_data)

    class Meta(CustomUserSerializer.Meta):
        extra_kwargs = {
            **{'password': {'read_only': True}},
        }
