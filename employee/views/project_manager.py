from rest_framework import generics

from employee.serializers import (
    TeamChangeSerializer,
)
from employee.views.generics import BaseConfigurationProjectManagersViewGeneric
from employee.views.service.teamChangeDelete import (
    ChangePersonalTeamViewMixin,
    DeletePersonalTeamViewMixin,
)
from general import (
    ViewsSerializerValidateRequestMixin,
    response_true_message_schema,
    response_true_request_false_message_schema
)


class AllProjectManagerListAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.ListAPIView
):
    pass


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


class ProjectManagerChangeTeamAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.GenericAPIView,
    ChangePersonalTeamViewMixin,
    ViewsSerializerValidateRequestMixin
):
    serializer_class = TeamChangeSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        team_name = self._validate_request(request).data['team']

        return self._post_change_team(
            f'Team for this project manager now \'{team_name}\'',
            team_name
        )


class ProjectManagerDeleteTeamAPIView(
    BaseConfigurationProjectManagersViewGeneric,
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):

    @response_true_request_false_message_schema
    def post(self, request, *args, **kwargs):
        return self._post_delete_team("Team for this project manager None")
