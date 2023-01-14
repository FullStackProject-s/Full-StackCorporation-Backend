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


class OrganizationListAPIVIew(
    BaseConfigurationOrganizationViewGeneric,
    generics.ListAPIView
):
    pass


class OrganizationRetrieveAPIView(
    BaseConfigurationOrganizationViewGeneric,
    generics.RetrieveAPIView
):
    pass


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
