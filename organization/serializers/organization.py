from organization.serializers.generic import BaseOrganizationSerializer

from user.serializers import CustomUserShowSerializer
from project.serializer import ProjectShowSerializer


class OrganizationShowSerializer(BaseOrganizationSerializer):
    owner = CustomUserShowSerializer(read_only=True)
    projects = ProjectShowSerializer(many=True, read_only=True)
    members = CustomUserShowSerializer(many=True, read_only=True)


class OrganizationSerializer(BaseOrganizationSerializer):
    def to_representation(self, instance):
        return OrganizationShowSerializer(instance).save()
