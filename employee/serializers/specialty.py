from employee.serializers import DeveloperSerializer

from employee.serializers.generics import BaseDeveloperOrgSpecialtySerializer
from organization.serializers import OrganizationSerializer


class DeveloperOrgSpecialtyShowSerializer(BaseDeveloperOrgSpecialtySerializer):
    organization_developer = DeveloperSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)


class DeveloperOrgSpecialtySerializer(BaseDeveloperOrgSpecialtySerializer):
    def to_representation(self, instance):
        return DeveloperOrgSpecialtyShowSerializer(instance).data
