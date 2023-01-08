from rest_framework import serializers

from organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Organization
        fields = (
            'pk',
            'organization_name',
            'owner'

        )
