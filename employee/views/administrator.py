from rest_framework import generics

from .mixins import BaseConfigurationAdministratorsViewMixin


class AllAdministratorsListAPIView(
    BaseConfigurationAdministratorsViewMixin,
    generics.ListAPIView
):
    pass


class AdministratorRetrieveAPIView(
    BaseConfigurationAdministratorsViewMixin,
    generics.RetrieveAPIView
):
    pass


class AdministratorCreateAPIView(
    BaseConfigurationAdministratorsViewMixin,
    generics.CreateAPIView
):
    pass


class AdministratorDestroyAPIView(
    BaseConfigurationAdministratorsViewMixin,
    generics.DestroyAPIView
):
    pass


class AdministratorUpdateAPIView(
    BaseConfigurationAdministratorsViewMixin,
    generics.UpdateAPIView
):
    pass