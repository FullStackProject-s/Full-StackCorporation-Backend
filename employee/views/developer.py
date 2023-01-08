from rest_framework import generics

from .generics import BaseConfigurationDevelopersViewGeneric

from employee.serializers import (
    DeveloperStackTechnologiesSerializer,
)
from employee.views.mixins import DeveloperTechnologiesRemoveUpdate

from general.schemas import (
    response_true_message_schema,
)
from general.mixins import (
    ViewsSerializerValidateRequestMixin,
)


class AllDeveloperListAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.ListAPIView
):
    pass


class DeveloperRetrieveAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.RetrieveAPIView
):
    pass


class DeveloperCreateAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.CreateAPIView
):
    pass


class DeveloperDestroyAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.DestroyAPIView
):
    pass


class DeveloperUpdateAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.UpdateAPIView
):
    pass


class DeveloperAddStackTechnologies(
    BaseConfigurationDevelopersViewGeneric,
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin,
    DeveloperTechnologiesRemoveUpdate
):
    serializer_class = DeveloperStackTechnologiesSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        dev = self.get_object()
        return self._change_technologies(
            request,
            "Tech for this developer set",
            dev.append_technologies
        )


class DeveloperRemoveTechnologies(
    BaseConfigurationDevelopersViewGeneric,
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin,
    DeveloperTechnologiesRemoveUpdate
):
    serializer_class = DeveloperStackTechnologiesSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        dev = self.get_object()
        return self._change_technologies(
            request,
            "Tech for this developer unset",
            dev.remove_technologies
        )
