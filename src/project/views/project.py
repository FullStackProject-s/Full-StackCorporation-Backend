from rest_framework import generics

from .generics import BaseConfigurationProjectsViewGeneric
from project.models import Project


class ProjectsListAPIVIew(
    BaseConfigurationProjectsViewGeneric,
    generics.ListAPIView
):
    queryset = Project.objects.prefetch_related('teams')


class ProjectsRetrieveAPIView(
    BaseConfigurationProjectsViewGeneric,
    generics.RetrieveAPIView
):
    queryset = Project.objects.prefetch_related('teams')


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
