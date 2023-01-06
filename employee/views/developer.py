from rest_framework import generics

from .generics import BaseConfigurationDevelopersViewGeneric

from employee.models import (
    Technologies
)
from employee.serializers import (
    DeveloperStackTechnologiesSerializer
)
from employee.serializers import TeamChangeSerializer
from employee.views.service.teamChangeDelete import (
    ChangePersonalTeamViewMixin,
    DeletePersonalTeamViewMixin
)

from general import (
    ViewsSerializerValidateRequestMixin,
    PostResponse,
    response_true_message_schema,
    response_true_request_false_message_schema
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
    ViewsSerializerValidateRequestMixin
):
    serializer_class = DeveloperStackTechnologiesSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        dev = self.get_object()

        if tech := Technologies.objects.filter(
                technology_name=self._validate_request(request).data[
                    'technology_name'
                ]
        ).first():
            dev.append_technologies(tech.first())
            return PostResponse.response_ok(
                f"{tech.technology_name} for this developer set"
            )
        return PostResponse.not_found_response('Tech not found')


class DeveloperRemoveTechnologies(
    BaseConfigurationDevelopersViewGeneric,
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin
):
    serializer_class = DeveloperStackTechnologiesSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        dev = self.get_object()

        if tech := Technologies.objects.filter(
                technology_name=self._validate_request(request).data[
                    'technology_name'
                ]
        ).first():
            dev.remove_technologies(tech)
            return PostResponse.response_ok(
                f"{tech.technology_name} for this developer unset"
            )
        return PostResponse.not_found_response('Tech not found')
