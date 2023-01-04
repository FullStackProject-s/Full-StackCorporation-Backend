from rest_framework import serializers
from employee.models import Administrator

from user.serializers.profile import ProfileSerializer


class AdministratorSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Administrator
        fields = (
            'pk',
            'profile',
        )
