from rest_framework import generics

from .generics import BaseConfigurationAdministratorsViewGeneric
from .mixins import MeAPIViewMixin


class AllAdministratorsListAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.ListAPIView
):
    pass


class AdministratorMeAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.RetrieveAPIView,
    MeAPIViewMixin
):
    def get_object(self):
        return self._get_me_object_or_404()


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
