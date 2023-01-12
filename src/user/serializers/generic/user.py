from rest_framework import serializers

from user.admin import User


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
            'staff_role'

        )
        extra_kwargs = {'staff_role': {'required': False}}
