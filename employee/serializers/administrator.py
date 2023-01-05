from django.db import transaction
from rest_framework import serializers

from employee.models import Administrator
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)

from user.serializers.mixins import CreateCustomUserSerializerMixin
from user.serializers.profile import ProfileSerializer


class AdministratorSerializer(
    serializers.ModelSerializer,
    CreateCustomUserSerializerMixin,
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
):
    profile = ProfileSerializer()

    class Meta:
        model = Administrator
        fields = (
            'pk',
            'profile',
        )

    def create(self, validated_data):
        with transaction.atomic():
            return self._staff_create(validated_data, 'admin')

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
