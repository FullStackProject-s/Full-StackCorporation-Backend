from rest_framework import generics

from .generics import BaseConfigurationDevelopersViewGeneric

from employee.serializers import (
    DeveloperStackTechnologiesSerializer,
    TeamChangeSerializer
)
from employee.views.mixins import (
    ChangePersonalTeamViewMixin,
    DeletePersonalTeamViewMixin, DeveloperTechnologiesRemoveUpdate
)

from general.schemas import (
    response_true_message_schema,
    response_true_request_false_message_schema
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


class DeveloperUpdateTeamAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.GenericAPIView,
    ChangePersonalTeamViewMixin,
    ViewsSerializerValidateRequestMixin
):
    serializer_class = TeamChangeSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        team_name = self._validate_request(request).data['team']

        return self._post_change_team(
            f'Team for this developer now \'{team_name}\'',
            team_name
        )


class DeveloperDeleteTeamAPIView(
    BaseConfigurationDevelopersViewGeneric,
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):
    @response_true_request_false_message_schema
    def post(self, request, *args, **kwargs):
        return self._post_delete_team('Team for this developer now NULL')


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
