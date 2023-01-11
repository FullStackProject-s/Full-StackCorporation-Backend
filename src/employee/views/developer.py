from rest_framework import generics

from .generics import BaseConfigurationDevelopersViewGeneric


class AllDeveloperListAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.ListAPIView
):
    pass


class DeveloperRetrieveAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.RetrieveAPIView
):
    pass


class DeveloperCreateAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.CreateAPIView
):
    pass


class DeveloperDestroyAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.DestroyAPIView
):
    pass


class DeveloperUpdateAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.UpdateAPIView
):
    pass
