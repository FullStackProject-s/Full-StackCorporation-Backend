from rest_framework import serializers

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from user.serializers import CustomUserShowSerializer


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
