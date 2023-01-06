from rest_framework import generics

from .mixins import BaseConfigurationDevelopersViewMixin

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
    BaseConfigurationDevelopersViewMixin,
    generics.ListAPIView
):
    pass


class DeveloperRetrieveAPIView(
    BaseConfigurationDevelopersViewMixin,
    generics.RetrieveAPIView
):
    pass


class DeveloperCreateAPIView(
    BaseConfigurationDevelopersViewMixin,
    generics.CreateAPIView
):
    pass


class DeveloperDestroyAPIView(
    BaseConfigurationDevelopersViewMixin,
    generics.DestroyAPIView
):
    pass


class DeveloperUpdateAPIView(
    BaseConfigurationDevelopersViewMixin,
    generics.UpdateAPIView
):
    pass


class DeveloperUpdateTeamAPIView(
    BaseConfigurationDevelopersViewMixin,
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
    BaseConfigurationDevelopersViewMixin,
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):
    @response_true_request_false_message_schema
    def post(self, request, *args, **kwargs):
        return self._post_delete_team('Team for this developer now NULL')


class DeveloperAddStackTechnologies(
    BaseConfigurationDevelopersViewMixin,
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
    BaseConfigurationDevelopersViewMixin,
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
