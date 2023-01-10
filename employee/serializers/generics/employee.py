from rest_framework import serializers

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from employee.models import (
    ProjectManager,
    Developer,
    Administrator
)


class BaseStaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'pk',
            'profile',
        )


class BaseManagerDeveloperSerializer(BaseStaffSerializer):
    team = serializers.SerializerMethodField(
        read_only=True,
        required=False
    )

    class Meta(BaseStaffSerializer.Meta):
        fields = (
            *BaseStaffSerializer.Meta.fields,
            'team',
        )

    @extend_schema_field(OpenApiTypes.STR)
    def get_team(self, obj):
        if obj.team:
            return obj.team.team_name
        return None


class BaseProjectManagerSerializer(BaseManagerDeveloperSerializer):
    class Meta:
        model = ProjectManager
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
        )


class BaseAdministratorSerializer(BaseStaffSerializer):
    class Meta:
        model = Administrator
        fields = (
            *BaseStaffSerializer.Meta.fields,
        )


class BaseDeveloperSerializer(BaseManagerDeveloperSerializer):
    class Meta(BaseManagerDeveloperSerializer.Meta):
        model = Developer
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
            'skill_level',
            'specialties',
            'stack',
        )
