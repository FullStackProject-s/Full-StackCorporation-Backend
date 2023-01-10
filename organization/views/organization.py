from rest_framework import generics

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
