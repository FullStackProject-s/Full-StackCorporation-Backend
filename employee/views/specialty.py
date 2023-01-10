from rest_framework import generics

from employee.views.generics import (
    BaseDeveloperOrganizationSpecialtyViewGeneric
)


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
    pass
