from django.contrib.auth import get_user_model

from user.serializers.permission import PermissionSerializer
from user.serializers.generic import BaseCustomUserSerializer

User = get_user_model()


class CustomUserShowSerializer(BaseCustomUserSerializer):
    staff_role = PermissionSerializer(
        required=False,
        read_only=True
    )


class CustomUserSerializer(BaseCustomUserSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, data):
        return CustomUserShowSerializer(data).data

    class Meta(BaseCustomUserSerializer.Meta):
        fields = (
            *BaseCustomUserSerializer.Meta.fields,
            'password',
        )
