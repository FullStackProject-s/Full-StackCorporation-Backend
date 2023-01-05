from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from employee.models.employees import Developer
from employee.models.technologies import Technologies
from employee.serializers.technologies import TechnologiesSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffCreateSerializerMixin
)
from employee.serializers.schemas.developer import developer_change_team

from user.serializers.profile import ProfileSerializer
from user.serializers.mixins import CreateCustomUserSerializerMixin


class DeveloperSerializer(
    serializers.ModelSerializer,
    ProfileUpdateSerializerMixin,
    CreateCustomUserSerializerMixin,
    StaffCreateSerializerMixin
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
    specialty = serializers.CharField(source='get_specialty_display')

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
            specialty = validated_data.pop('get_specialty_display')
            return self._staff_create(
                validated_data,
                'dev',
                specialty=specialty
            )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
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
