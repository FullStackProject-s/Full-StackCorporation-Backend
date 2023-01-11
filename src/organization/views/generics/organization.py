from drf_spectacular.utils import extend_schema
from rest_framework import generics

from organization.models import Organization
from organization.serializers import (
    OrganizationSerializer,
    OrganizationShowSerializer
)


@extend_schema(responses=OrganizationShowSerializer)
class BaseConfigurationOrganizationViewGeneric(generics.GenericAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
