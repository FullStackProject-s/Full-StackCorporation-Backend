from rest_framework import serializers

from employee.serializers import DeveloperSerializer

from employee.serializers.generics import BaseDeveloperOrgSpecialtySerializer


class DeveloperOrgSpecialtyShowSerializer(BaseDeveloperOrgSpecialtySerializer):
    organization_developer = DeveloperSerializer(read_only=True)
    organization = serializers.SerializerMethodField()

    def get_organization(self, obj):
        if obj.organization:
            return obj.organization.organization_name
        return None


class DeveloperOrgSpecialtySerializer(BaseDeveloperOrgSpecialtySerializer):
    def to_representation(self, instance):
        return DeveloperOrgSpecialtyShowSerializer(instance).data


class DeveloperOrgSpecialtyUpdateSerializer(DeveloperOrgSpecialtySerializer):
    class Meta(DeveloperOrgSpecialtySerializer.Meta):
        fields = (
            'specialty',
        )
