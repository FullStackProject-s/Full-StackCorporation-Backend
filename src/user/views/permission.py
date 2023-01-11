from rest_framework import generics

from user.views.generics import BaseConfigurationPermissionViewGeneric


class AllPermissionListAPIView(
    BaseConfigurationPermissionViewGeneric,
    generics.ListAPIView
):
    pass


class PermissionRetrieveAPIView(
    BaseConfigurationPermissionViewGeneric,
    generics.RetrieveAPIView
):
    pass


class PermissionCreateAPIView(
    BaseConfigurationPermissionViewGeneric,
    generics.CreateAPIView
):
    pass


class PermissionDestroyAPIView(
    BaseConfigurationPermissionViewGeneric,
    generics.DestroyAPIView
):
    pass
