from rest_framework import generics

from .generics import BaseConfigurationAdministratorsViewGeneric


class AllAdministratorsListAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.ListAPIView
):
    pass


class AdministratorRetrieveAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.RetrieveAPIView
):
    pass


class AdministratorCreateAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.CreateAPIView
):
    pass


class AdministratorDestroyAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.DestroyAPIView
):
    pass


class AdministratorUpdateAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.UpdateAPIView
):
    pass
