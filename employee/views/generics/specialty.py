from rest_framework import generics

from employee.models import DeveloperOrganizationSpecialty
from employee.serializers import DeveloperOrgSpecialtyPOSTSerializer


class BaseDeveloperOrganizationSpecialtyViewGeneric(generics.GenericAPIView):
    serializer_class = DeveloperOrgSpecialtyPOSTSerializer
    queryset = DeveloperOrganizationSpecialty.objects.all()
