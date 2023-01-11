from rest_framework import generics

from project.views.generics.team import TeamBaseGenericView


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


class TeamDestroyAPIView(
    TeamBaseGenericView,
    generics.DestroyAPIView
):
    pass


class TeamCreateAPIView(
    TeamBaseGenericView,
    generics.CreateAPIView,
):
    pass


class TeamUpdateAPIView(
    TeamBaseGenericView,
    generics.UpdateAPIView,
):
    pass
