from rest_framework import (
    status,
    generics
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from organization.serializers import (
    OrganizationImageUploadSerializer,
    OrganizationShowSerializer
)
from .generics import BaseConfigurationOrganizationViewGeneric
from organization.models import Organization


class OrganizationListAPIVIew(
    BaseConfigurationOrganizationViewGeneric,
    generics.ListAPIView
):
    queryset = Organization.objects. \
        prefetch_related('members')


class OrganizationRetrieveAPIView(
    BaseConfigurationOrganizationViewGeneric,
    generics.RetrieveAPIView
):
    queryset = Organization.objects. \
        prefetch_related('members')


class OrganizationCreateAPIView(
    BaseConfigurationOrganizationViewGeneric,
    generics.CreateAPIView
):
    pass


class OrganizationDestroyAPIView(
    BaseConfigurationOrganizationViewGeneric,
    generics.DestroyAPIView
):
    pass


class OrganizationUpdateAPIView(
    BaseConfigurationOrganizationViewGeneric,
    generics.UpdateAPIView
):
    pass


class OrganizationUploadImageAPIView(BaseConfigurationOrganizationViewGeneric):
    serializer_class = OrganizationImageUploadSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        org = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if org.organization_avatar:
            org.organization_avatar.delete()

        org.organization_avatar = serializer.validated_data.get(
            'organization_avatar'
        )
        org.save()

        return Response(
            OrganizationShowSerializer(org).data,
            status=status.HTTP_202_ACCEPTED
        )
