from rest_framework import serializers

from drf_spectacular.utils import (
    extend_schema_field,
    inline_serializer
)
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

    @extend_schema_field(inline_serializer(
        name='team',
        fields={
            "pk": serializers.IntegerField(),
            "team_name": serializers.CharField(),
        }
    ))
    def get_team(self, obj):
        if obj.team:
            return {'pk': obj.team.pk, 'team_name': obj.team.team_name}
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
