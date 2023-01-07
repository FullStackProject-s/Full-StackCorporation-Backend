from rest_framework import generics

from employee.models import Developer

from general.mixins import ViewsSerializerValidateRequestMixin
from general.schemas import response_true_message_schema
from general.services import response_many_to_many_api_views

from project.serializer import (
    TeamNameSerializer,
    TeamTeamLeadSerializer,
    TeamProjectManagerSerializer,
    TeamDevelopersSerializer
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


class TeamUpdateDevelopersAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
):
    serializer_class = TeamDevelopersSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        team = self.get_object()
        developer_list = []
        developers_names = self._validate_request(request).data['developers']

        for developer_name in developers_names:
            if developer := Developer.objects.filter(
                    profile__user__username=developer_name
            ).first():
                team.append_developer(developer)
                developer_list.append(developer)
                developer.team = team

                team.save()
                developer.save()
        return response_many_to_many_api_views(
            developer_list,
            f"Developers for this team set",
            'Developers not found'
        )


class TeamRemoveDevelopersAPIView(
    TeamBaseGenericView,
    ViewsSerializerValidateRequestMixin,
):
    serializer_class = TeamDevelopersSerializer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        team = self.get_object()
        developer_list = []
        developers_names = self._validate_request(request).data['developers']

        for developer_name in developers_names:
            if developer := Developer.objects.filter(
                    profile__user__username=developer_name
            ).first():
                team.remove_developer(developer)
                developer_list.append(developer)
                developer.team = None

                team.save()
                developer.save()
        return response_many_to_many_api_views(
            developer_list,
            f"Developers for this team unset",
            'Developers not found'
        )
