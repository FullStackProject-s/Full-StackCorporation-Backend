from rest_framework import generics
from project.serializer.team import (
    TeamSerializer,
    TeamNameSerializer
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
