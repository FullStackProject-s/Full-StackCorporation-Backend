from rest_framework import generics

from employee.views.mixins import BaseConfigurationTechnologiesViewMixin


class AllTechnologiesListAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass


class TechnologiesRetrieveAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass


class TechnologiesCreateAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass


class TechnologiesDestroyAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass


class TechnologiesUpdateAPIView(
    BaseConfigurationTechnologiesViewMixin,
    generics.ListAPIView
):
    pass
