from rest_framework import generics

from employee.views.generics import (
    BaseDeveloperOrganizationSpecialtyViewGeneric
)
from employee.serializers import DeveloperOrgUpdateSpecialtySerializer


class DeveloperOrganizationSpecialtyListAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.ListAPIView
):
    pass


class DeveloperOrganizationSpecialtyRetrieveAPIView(
    BaseDeveloperOrganizationSpecialtyViewGeneric,
    generics.RetrieveAPIView
):
    pass


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
    serializer_class = DeveloperOrgUpdateSpecialtySerializer
