from django.db import transaction
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field, extend_schema_serializer
from rest_framework import serializers

from employee.models.employees import Developer
from employee.models.technologies import Technologies
from employee.serializers.schemas.developer import developer_change_team
from employee.serializers.technologies import TechnologiesSerializer

from user.serializers.profile import ProfileSerializer
from user.serializers.mixins.create_custom_user import \
    CreateCustomUserSerializerMixin


@extend_schema_serializer(
    exclude_fields=('team',)
)
class DeveloperSerializer(
    serializers.ModelSerializer,
    CreateCustomUserSerializerMixin
):
    profile = ProfileSerializer()
    stack = TechnologiesSerializer(many=True, required=False)
    team = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Developer
        fields = (
            'profile',
            'specialty',
            'stack',
            'team'
        )

    def create(self, validated_data):
        with transaction.atomic():
            _profile = self._create_profile(validated_data.pop('profile'))
            tech_list = []
            for item in validated_data.pop('stack'):
                tech_list.append(Technologies.objects.create(**item))
            dev = Developer.objects.create(**validated_data, profile=_profile)
            dev.append_technologies(tech_list)
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
class DeveloperSerializerChangeTeam(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            'team',
        )
