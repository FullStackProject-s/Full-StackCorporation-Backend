from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.serializers.permission import PermissionSerializer

User = get_user_model()


class BaseCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'create_at',
            'password',
            'staff_role'

        )
        extra_kwargs = {'staff_role': {'required': False}}


class CustomUserShowSerializer(BaseCustomUserSerializer):
    staff_role = PermissionSerializer(
        required=False,
        read_only=True
    )


class CustomUserSerializer(BaseCustomUserSerializer):
    def to_representation(self, data):
        return CustomUserShowSerializer(data).data
