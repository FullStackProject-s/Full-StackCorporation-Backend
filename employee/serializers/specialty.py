from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from employee.models import DeveloperOrganizationSpecialty
from employee.serializers import DeveloperSerializer

from employee.serializers.generics import BaseDeveloperOrgSpecialtySerializer
from organization.serializers import OrganizationSerializer


class DeveloperOrgSpecialtyGETSerializer(BaseDeveloperOrgSpecialtySerializer):
    organization_developer = DeveloperSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)


class DeveloperOrgSpecialtyPOSTSerializer(BaseDeveloperOrgSpecialtySerializer):
    def to_representation(self, instance):
        return DeveloperOrgSpecialtyGETSerializer(instance).data
