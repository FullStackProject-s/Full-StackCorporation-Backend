from rest_framework import generics

from .generics import BaseConfigurationDevelopersViewGeneric
from .mixins import MeAPIViewMixin


class AllDeveloperListAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.ListAPIView
):
    pass


class DeveloperMeAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.RetrieveAPIView,
    MeAPIViewMixin
):
    def get_object(self):
        return self._get_me_object_or_404()


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
