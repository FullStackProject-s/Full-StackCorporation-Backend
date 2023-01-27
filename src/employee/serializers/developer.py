from drf_spectacular.plumbing import build_array_type
from rest_framework import serializers

from drf_spectacular.utils import (
    extend_schema_field,
    inline_serializer
)

from employee.serializers.generics import BaseDeveloperSerializer
from employee.serializers.technologies import TechnologiesSerializer
from employee.serializers.services import set_perms_for_employee

from user.models.consts import StaffRole
from user.serializers import ProfileShowSerializer


class SpecialtySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    specialty = serializers.CharField()
    organization_name = serializers.CharField()


class DeveloperShowSerializer(BaseDeveloperSerializer):
    stack = TechnologiesSerializer(
        many=True,
        required=False,
        read_only=True
    )
    specialties = serializers.SerializerMethodField()
    profile = ProfileShowSerializer(read_only=True)

    @extend_schema_field((inline_serializer(
        name='specialties',
        fields={
            'specialties': serializers.ListSerializer(
                child=SpecialtySerializer()
            )
        }
    )))
    def get_specialties(self, obj):
        if obj.specialties:
            return [
                {
                    "pk": specialty.pk,
                    'specialty': specialty.specialty,
                    'organization_name': specialty.organization.organization_name
                }
                for specialty in
                obj.specialties.prefetch_related('organization')
            ]
        return None


class DeveloperSerializer(BaseDeveloperSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        set_perms_for_employee(StaffRole.DEVELOPER, instance)
        return instance

    def to_representation(self, instance):
        return DeveloperShowSerializer(instance).data
