from rest_framework import generics

from organization.models import Organization
from organization.serializers import OrganizationSerializer


class OrganizationGenericView(generics.GenericAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
