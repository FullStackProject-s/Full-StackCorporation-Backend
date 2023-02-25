from employee.serializers import DeveloperSerializer
from employee.serializers.generics import BaseDeveloperOrgSpecialtySerializer

from organization.serializers import OrganizationShowProjectsSerializer


class DeveloperOrgSpecialtyShowSerializer(BaseDeveloperOrgSpecialtySerializer):
    organization_developer = DeveloperSerializer(read_only=True)
    organization = OrganizationShowProjectsSerializer()


class DeveloperOrgSpecialtySerializer(BaseDeveloperOrgSpecialtySerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.organization_developer.append_specialties(instance)
        return instance

    def to_representation(self, instance):
        return DeveloperOrgSpecialtyShowSerializer(instance).data


class DeveloperOrgSpecialtyUpdateSerializer(DeveloperOrgSpecialtySerializer):
    class Meta(DeveloperOrgSpecialtySerializer.Meta):
        fields = (
            'specialty',
        )
