from rest_framework import generics

from employee.views.generics import BaseConfigurationProjectManagersViewGeneric
from employee.views.mixins import MeAPIViewMixin


class AllProjectManagerListAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.ListAPIView
):
    pass


class ProjectManagerAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.RetrieveAPIView,
    MeAPIViewMixin
):
    def get_object(self):
        return self._get_me_object_or_404()


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
