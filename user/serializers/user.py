from rest_framework import serializers
from django.contrib.auth import get_user_model

from user.models.utility import Permissions
from user.serializers.permission import PermissionSerializer

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer(source='staff_role')

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'create_at',
            'update_at',
            'password',
            'permission'
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data):
        password = validated_data.pop('password', None)
        _perm = validated_data.pop('staff_role', None)
        perm = Permissions.objects.get(role_name=_perm['role_name'])
        setattr(instance, 'staff_role', perm)

        if password is not None:
            instance.set_password(password)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
