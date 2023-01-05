from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from employee.models.employees import Developer
from employee.models.technologies import Technologies
from employee.serializers.schemas.developer import developer_change_team
from employee.serializers.technologies import TechnologiesSerializer

from user.models import Permissions, CustomUser
from user.serializers.profile import ProfileSerializer
from user.serializers.mixins.create_custom_user import \
    CreateCustomUserSerializerMixin


class DeveloperSerializer(
    serializers.ModelSerializer,
    CreateCustomUserSerializerMixin
):
    pk = serializers.IntegerField(read_only=True)
    profile = ProfileSerializer()
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )
    team = serializers.SerializerMethodField(
        read_only=True,
        required=False
    )

    class Meta:
        model = Developer
        fields = (
            'pk',
            'profile',
            'specialty',
            'stack',
            'team'
        )

    def create(self, validated_data):
        with transaction.atomic():
            _profile = self._create_profile(validated_data.pop('profile'))
            dev = Developer.objects.create(
                **validated_data,
                profile=_profile
            )
            permission, created_ = Permissions.objects.get_or_create(
                role_name='dev'
            )
            c = CustomUser.objects.get(username=dev.profile.user.username)
            c.staff_role = permission
            dev.profile.user.staff_role = permission
            c.save()
            return dev

    def update(self, instance, validated_data):

        profile_serializer = self.fields['profile']
        stack_serializer = self.fields['stack']
        if data := validated_data.pop('profile', None):
            profile_serializer.update(instance.profile, data)
        if data := validated_data.pop('stack', None):
            stack_serializer.update(instance.stack, data)
        return super().update(instance, validated_data)

    @extend_schema_field(OpenApiTypes.STR)
    def get_team(self, obj: Developer):
        if obj.team:
            return obj.team.team_name
        return "unknown"


@developer_change_team
class DeveloperChangeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            'pk',
            'team',
        )


class DeveloperAddStackTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = (
            'pk',
            'technology_name',
        )
