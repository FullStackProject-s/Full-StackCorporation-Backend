from rest_framework import generics

from employee.models import (
    ProjectManager,
    Developer
)
from project.models import Team
from project.serializer import TeamSerializer


class TeamBaseGenericRemoveUpdateMainPersonal:
    personal_model = None
    personal_relation_name = None


class TeamBaseGenericView(generics.GenericAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamProjectManagerRemoveUpdateBase(
    TeamBaseGenericRemoveUpdateMainPersonal
):
    personal_relation_name = 'project_manager'
    personal_model = ProjectManager


class TeamTeamLeadRemoveUpdateBase(
    TeamBaseGenericRemoveUpdateMainPersonal
):
    personal_relation_name = 'team_lead'
    personal_model = Developer
