from drf_spectacular.utils import extend_schema
from rest_framework import generics

from message.serializers import (
    InviteToOrganizationSerializer,
    InviteToOrganizationShowSerializer
)
from message.models import InviteToOrganization


@extend_schema(responses=InviteToOrganizationShowSerializer)
class BaseInviteToOrganizationViewGeneric(generics.GenericAPIView):
    serializer_class = InviteToOrganizationSerializer
    queryset = InviteToOrganization.objects.all()
