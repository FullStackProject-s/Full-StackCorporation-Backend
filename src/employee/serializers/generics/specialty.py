from rest_framework import serializers
from employee.models import DeveloperOrganizationSpecialty


class BaseDeveloperOrgSpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = DeveloperOrganizationSpecialty
        fields = (
            'pk',
            'specialty',
            'organization_developer',
            'organization',
        )
