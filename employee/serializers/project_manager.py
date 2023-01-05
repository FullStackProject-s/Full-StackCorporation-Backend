from django.db import transaction
from rest_framework import serializers

from employee.models import ProjectManager
from employee.serializers.mixins import ProfileUpdateSerializerMixin
from user.models import Permissions, CustomUser

from user.serializers.mixins import CreateCustomUserSerializerMixin
from user.serializers.profile import ProfileSerializer


class ProjectManagerSerializer(
    serializers.ModelSerializer,
    ProfileUpdateSerializerMixin,
    CreateCustomUserSerializerMixin
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
            _profile = self._create_profile(validated_data.pop('profile'))

            prod_manager = ProjectManager.objects.create(
                **validated_data,
                profile=_profile,
            )
            permission, created_ = Permissions.objects.get_or_create(
                role_name='prod manager'
            )
            c = CustomUser.objects.get(
                username=prod_manager.profile.user.username
            )
            c.staff_role = permission
            c.save()
            prod_manager.profile.user.staff_role = permission
            return prod_manager

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)
