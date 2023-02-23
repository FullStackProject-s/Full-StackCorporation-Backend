from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models.consts import StaffRole
User = get_user_model()


class BaseCustomUserSerializer(serializers.ModelSerializer):
    staff_role = serializers.ChoiceField(
        choices=StaffRole.choices
    )

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
