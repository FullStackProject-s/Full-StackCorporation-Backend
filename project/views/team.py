from rest_framework import generics

from employee.models import Developer, ProjectManager
from general import ViewsSerializerValidateRequestMixin

from general.schemas import (
    response_true_message,
    response_true_request_false_message
)

from general.services import PostResponse

from project.serializer import (
    TeamSerializer,
    TeamNameSerializer,
    TeamTeamLeadSerializer,
    TeamProjectManagerSerializer
)
from project.models.team import Team


class AllTeamListAPIView(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamCreateAPIView(generics.CreateAPIView):
    serializer_class = TeamNameSerializer


class TeamChangeNameAPIView(generics.UpdateAPIView):
    serializer_class = TeamNameSerializer
    queryset = Team.objects.all()


class TeamUpdateTeamLeadAPIView(
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin
):
    serializer_class = TeamTeamLeadSerializer
    queryset = Team.objects.all()

    @response_true_message
    def post(self, request, *args, **kwargs):
        team = self.get_object()

        team_lead = self._validate_request(request).data['team_lead']

        if dev := Developer.objects.filter(profile__user__username=team_lead):
            team.team_lead = dev.first()
            team.save()
            return PostResponse.response_ok(
                f"Team lead for this team \'{team_lead}\'"
            )
        return PostResponse.not_found_response('Not found team lead')


class TeamRemoveTeamLeadAPIView(generics.GenericAPIView):
    serializer_class = TeamTeamLeadSerializer
    queryset = Team.objects.all()

    @response_true_request_false_message
    def post(self, request, *args, **kwargs):
        team = self.get_object()

        team.team_lead = None
        team.save()
        return PostResponse.response_ok(
            f"Team lead for this team NULL"
        )


class TeamUpdateProjectManagerAPIView(
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin
):
    serializer_class = TeamProjectManagerSerializer
    queryset = Team.objects.all()

    @response_true_message
    def post(self, request, *args, **kwargs):
        team = self.get_object()

        project_manager = self._validate_request(request).data[
            'project_manager'
        ]
        if proj_manager := ProjectManager.objects.filter(
                profile__user__username=project_manager
        ):
            team.project_manager = proj_manager.first()
            team.save()
            return PostResponse.response_ok(
                f"Project manager for this team \'{project_manager}\'"
            )
        return PostResponse.not_found_response('Not found project manager')


class TeamRemoveProjectManagerAPIView(generics.GenericAPIView):
    serializer_class = TeamProjectManagerSerializer
    queryset = Team.objects.all()

    @response_true_request_false_message
    def post(self, request, *args, **kwargs):
        team = self.get_object()

        team.project_manager = None
        team.save()
        return PostResponse.response_ok(
            f"Project manager for this team NULL"
        )
