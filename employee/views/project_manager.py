from rest_framework import generics

from employee.views.generics import BaseConfigurationProjectManagersViewGeneric


class AllProjectManagerListAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.ListAPIView
):
    pass


class ProjectManagerRetrieveAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.RetrieveAPIView
):
    pass


class ProjectManagerCreateAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.CreateAPIView
):
    pass


class ProjectManagerDestroyAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.DestroyAPIView
):
    pass


class ProjectManagerUpdateAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.UpdateAPIView
):
    pass
