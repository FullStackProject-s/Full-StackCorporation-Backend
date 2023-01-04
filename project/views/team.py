from rest_framework import generics
from project.serializer.team import TeamSerializer
from project.models.team import Team


class AllTeamListAPIView(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamCreateAPIView(generics.CreateAPIView):
    serializer_class = TeamSerializer
