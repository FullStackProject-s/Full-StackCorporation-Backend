from drf_spectacular.utils import extend_schema
from rest_framework import generics

from employee.views.generics import \
    BaseDeveloperOrganizationSpecialtyViewGeneric
from employee.serializers import DeveloperOrgSpecialtyGETSerializer


class DeveloperOrganizationSpecialtyListAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.ListAPIView
):
    serializer_class = DeveloperOrgSpecialtyGETSerializer


class DeveloperOrganizationSpecialtyRetrieveAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.RetrieveAPIView
):
    serializer_class = DeveloperOrgSpecialtyGETSerializer


@extend_schema(responses=DeveloperOrgSpecialtyGETSerializer)
class DeveloperOrganizationSpecialtyCreateAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.CreateAPIView
):
    pass


class DeveloperOrganizationSpecialtyDestroyAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.DestroyAPIView
):
    pass


class DeveloperOrganizationSpecialtyUpdateAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.UpdateAPIView
):
    pass
