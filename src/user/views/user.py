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


class UserMeAPIView(
    BaseConfigurationUsersViewGeneric,
    generics.RetrieveAPIView
):
    def get(self, request, *args, **kwargs):
        self.get_object = lambda: request.user  # noqa
        return self.retrieve(request, *args, **kwargs)


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
