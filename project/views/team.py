from rest_framework import generics

from general import ViewsSerializerValidateRequestMixin
from general.schemas import response_true_message_schema

from project.serializer import (
    TeamNameSerializer,
    TeamTeamLeadSerializer,
    TeamProjectManagerSerializer
)
from project.views.generics.team import TeamBaseGenericView

from project.views.mixins import (
    TeamRemoveMainPersonalViewMixin,
    TeamUpdateMainPersonalViewMixin
)
from project.views.generics import (
    TeamProjectManagerRemoveUpdateBase,
    TeamTeamLeadRemoveUpdateBase
)


class AllTeamListAPIView(
    TeamBaseGenericView,
    generics.ListAPIView
):
    pass


class TeamRetrieveAPIView(
    TeamBaseGenericView,
    generics.RetrieveAPIView
):
    pass


class TeamCreateAPIView(
    TeamBaseGenericView,
    generics.CreateAPIView
):
    serializer_class = TeamNameSerializer


class TeamChangeNameAPIView(
    TeamBaseGenericView,
    generics.UpdateAPIView
):
    serializer_class = TeamNameSerializer


class TeamUpdateTeamLeadAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
    TeamTeamLeadRemoveUpdateBase,
    TeamUpdateMainPersonalViewMixin
):
    serializer_class = TeamTeamLeadSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._update_personal(
            request,
            'Team lead for this team set\'s'
        )


class TeamRemoveTeamLeadAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
    TeamTeamLeadRemoveUpdateBase,
    TeamRemoveMainPersonalViewMixin
):
    serializer_class = TeamTeamLeadSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._remove_personal(
            request,
            'Team lead for this team removed'
        )


class TeamUpdateProjectManagerAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
    TeamProjectManagerRemoveUpdateBase,
    TeamUpdateMainPersonalViewMixin
):
    serializer_class = TeamProjectManagerSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._update_personal(
            request,
            'Project manager for this team set\'s'
        )


class TeamRemoveProjectManagerAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
    TeamProjectManagerRemoveUpdateBase,
    TeamRemoveMainPersonalViewMixin
):
    serializer_class = TeamProjectManagerSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._remove_personal(
            request,
            'Project manager for this team removed'
        )


class TeamRemoveDevelopersAPIView: ...
