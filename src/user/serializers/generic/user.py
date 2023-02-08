from django.contrib.auth import get_user_model
from rest_framework import serializers

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
            'staff_role'

        )
        extra_kwargs = {'staff_role': {'required': False}}
