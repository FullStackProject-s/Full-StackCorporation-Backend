from django.db import transaction
from rest_framework import serializers

from employee.models import ProjectManager
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)

from user.serializers.mixins import CreateCustomUserSerializerMixin
from user.serializers.profile import ProfileSerializer


class ProjectManagerSerializer(
    serializers.ModelSerializer,
    ProfileUpdateSerializerMixin,
    CreateCustomUserSerializerMixin,
    StaffCreateSerializerMixin
):
    profile = ProfileSerializer()

    class Meta:
        model = ProjectManager
        fields = (
            'pk',
            'profile',
        )

    def create(self, validated_data):
        with transaction.atomic():
            return self._staff_create(validated_data, 'prod manager')

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
