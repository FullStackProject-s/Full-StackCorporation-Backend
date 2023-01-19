from drf_spectacular.utils import extend_schema
from rest_framework import (
    generics,
    permissions
)
from organization.models import Organization
from organization.serializers import (
    OrganizationSerializer,
    OrganizationShowSerializer
)
from organization.permissions import (
    IsAdministratorOrOwnerOrReadOnlyOrganization
)


@extend_schema(responses=OrganizationShowSerializer)
class BaseConfigurationOrganizationViewGeneric(generics.GenericAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyOrganization
    ]
