from rest_framework import serializers

from organization.models import Organization


class BaseOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'pk',
            'organization_name',
            'owner',
            'organization_avatar',
            'projects',
            'members',
        )
