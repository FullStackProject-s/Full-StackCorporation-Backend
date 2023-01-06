from rest_framework import generics

from employee.views.mixins import BaseConfigurationTechnologiesViewMixin


class AllTechnologiesListAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass


class TechnologiesRetrieveAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.RetrieveAPIView
):
    pass


class TechnologiesCreateAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.CreateAPIView
):
    pass


class TechnologiesDestroyAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.DestroyAPIView
):
    pass


class TechnologiesUpdateAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.UpdateAPIView
):
    pass
