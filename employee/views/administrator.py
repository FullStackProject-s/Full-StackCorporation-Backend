from rest_framework import generics

from general.schemas import create_only_employee_schema
from .generics import BaseConfigurationAdministratorsViewGeneric
from employee.serializers import (
    BaseCreatOnlySerializer,
)


class AllAdministratorsListAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.ListAPIView
):
    pass


class AdministratorRetrieveAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.RetrieveAPIView
):
    pass


# @create_only_employee_schema
class AdministratorCreateAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.CreateAPIView
):
    serializer_request_class = BaseCreatOnlySerializer


class AdministratorDestroyAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.DestroyAPIView
):
    pass


class AdministratorUpdateAPIView(
    BaseConfigurationAdministratorsViewGeneric,
    generics.UpdateAPIView
):
    pass
