from rest_framework import generics

from user.views.generics import BaseConfigurationProfilesViewGeneric


class AllProfileListAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.ListAPIView
):
    pass


class ProfileRetrieveAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.RetrieveAPIView
):
    pass


class ProfileCreateAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.CreateAPIView
):
    pass


class ProfileDestroyAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.DestroyAPIView
):
    pass


class ProfileUpdateAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.UpdateAPIView
):
    pass
