from rest_framework import serializers
from employee.models import DeveloperOrganizationSpecialty


class BaseDeveloperOrgSpecialtySerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = DeveloperOrganizationSpecialty
        fields = '__all__'

