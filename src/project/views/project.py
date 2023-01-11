from rest_framework import generics

from .generics import BaseConfigurationProjectsViewGeneric


class ProjectsListAPIVIew(
    BaseConfigurationProjectsViewGeneric,
    generics.ListAPIView
):
    pass


class ProjectsRetrieveAPIView(
    BaseConfigurationProjectsViewGeneric,
    generics.RetrieveAPIView
):
    pass


class ProjectCreateAPIView(
    BaseConfigurationProjectsViewGeneric,
    generics.CreateAPIView
):
    pass


class ProjectDestroyAPIView(
    BaseConfigurationProjectsViewGeneric,
    generics.DestroyAPIView
):
    pass


class ProjectUpdateAPIView(
    BaseConfigurationProjectsViewGeneric,
    generics.UpdateAPIView
):
    pass
