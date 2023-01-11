from rest_framework import generics

from employee.views.generics import BaseConfigurationTechnologiesViewGeneric


class AllTechnologiesListAPIView(
    BaseConfigurationTechnologiesViewGeneric,
    generics.ListAPIView
):
    pass


class TechnologiesRetrieveAPIView(
    BaseConfigurationTechnologiesViewGeneric,
    generics.RetrieveAPIView
):
    pass


class TechnologiesCreateAPIView(
    BaseConfigurationTechnologiesViewGeneric,
    generics.CreateAPIView
):
    pass


class TechnologiesDestroyAPIView(
    BaseConfigurationTechnologiesViewGeneric,
    generics.DestroyAPIView
):
    pass


class TechnologiesUpdateAPIView(
    BaseConfigurationTechnologiesViewGeneric,
    generics.UpdateAPIView
):
    pass
