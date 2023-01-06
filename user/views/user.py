from django.contrib.auth import get_user_model
from rest_framework import generics

from user.views.generics import BaseConfigurationUsersViewGeneric


class AllUsersListAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.ListAPIView
):
    pass


class UserRetrieveAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.RetrieveAPIView
):
    pass


class UserCreateAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.CreateAPIView
):
    pass


class UserDestroyAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.DestroyAPIView
):
    pass


class UserUpdateAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.UpdateAPIView
):
    pass
