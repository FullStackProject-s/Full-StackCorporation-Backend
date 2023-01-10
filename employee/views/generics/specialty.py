from drf_spectacular.utils import extend_schema
from rest_framework import generics

from employee.models import DeveloperOrganizationSpecialty
from employee.serializers import (
    DeveloperOrgSpecialtySerializer,
    DeveloperOrgSpecialtyShowSerializer
)


@extend_schema(responses=DeveloperOrgSpecialtyShowSerializer)
class BaseDeveloperOrganizationSpecialtyViewGeneric(generics.GenericAPIView):
    serializer_class = DeveloperOrgSpecialtySerializer
    queryset = DeveloperOrganizationSpecialty.objects.all()
