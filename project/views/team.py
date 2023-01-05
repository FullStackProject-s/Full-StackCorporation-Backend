from rest_framework import generics

from employee.models import Developer

from general.schemas import response_true_message
from general.services import PostResponse

from project.serializer import (
    TeamSerializer,
    TeamNameSerializer,
    TeamTeamLeadSerializer
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


class TeamUpdateTeamLeadAPIView(generics.GenericAPIView):
    serializer_class = TeamTeamLeadSerializer
    queryset = Team.objects.all()

    @response_true_message
    def post(self, request, *args, **kwargs):
        team = self.get_object()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        team_lead = serializer.data['team_lead']
        dev = Developer.objects.get(profile__user__username=team_lead)
        team.team_lead = dev
        team.save()
        return PostResponse.response_ok(
            f"Team lead for this team \'{team_lead}\'"
        )
