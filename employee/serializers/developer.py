from rest_framework import serializers

from employee.models.consts import Specialty
from employee.models.employees import Developer
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.technologies import TechnologiesSerializer
from employee.serializers.mixins import (
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin
)
from user.models.consts import StaffRole


class DeveloperSerializer(
    BaseManagerDeveloperSerializer,
    ProfileUpdateSerializerMixin,
    StaffPermissionsSetSerializerMixin
):
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )
    specialty = serializers.CharField(source='get_specialty_display')

    class Meta(BaseManagerDeveloperSerializer.Meta):
        model = Developer
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
            'specialty',
            'stack',
        )

    def validate(self, attrs):
        if attrs.get('get_specialty_display', None) not in Specialty.values:
            raise serializers.ValidationError("Incorrect specialty")
        return super().validate(attrs)

    def create(self, validated_data):
        specialty = validated_data.pop('get_specialty_display')
        obj = super().create(validated_data)
        obj.set_specialty(specialty)

        return self._set_permissions(
            obj,
            StaffRole.DEVELOPER,
        )

    def update(self, instance, validated_data):
        self._profile_update(instance, validated_data)
        return super().update(instance, validated_data)


class DeveloperChangeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            'pk',
            'team',
        )


class DeveloperStackTechnologiesSerializer(serializers.Serializer):
    technology_names = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        fields = (
            'technology_names',
        )
