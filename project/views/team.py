from rest_framework import generics

from employee.models import Developer, ProjectManager

from general import ViewsSerializerValidateRequestMixin
from general.schemas import response_true_message_schema
from general.services import PostResponse

from project.serializer import (
    TeamSerializer,
    TeamNameSerializer,
    TeamTeamLeadSerializer,
    TeamProjectManagerSerializer
)
from project.models.team import Team
from project.views.generics import (
    TeamGenericRemovePersonal,
    TeamGenericUpdatePersonal
)


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
    ViewsSerializerValidateRequestMixin,
    TeamGenericUpdatePersonal
):
    serializer_class = TeamTeamLeadSerializer
    queryset = Team.objects.all()

    personal_model = Developer
    personal_relation_name = 'team_lead'

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._update_personal(
            request,
            'Team lead for this team set\'s'
        )


class TeamRemoveTeamLeadAPIView(
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin,
    TeamGenericRemovePersonal
):
    serializer_class = TeamTeamLeadSerializer
    queryset = Team.objects.all()

    personal_relation_name = 'team_lead'
    personal_model = Developer

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._remove_personal(
            request,
            'Team lead for this team removed'
        )


class TeamUpdateProjectManagerAPIView(
    generics.GenericAPIView,
    ViewsSerializerValidateRequestMixin,
    TeamGenericUpdatePersonal
):
    serializer_class = TeamProjectManagerSerializer
    queryset = Team.objects.all()

    personal_model = ProjectManager
    personal_relation_name = 'project_manager'

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._update_personal(
            request,
            'Project manager for this team set\'s'
        )


class TeamRemoveProjectManagerAPIView(
    generics.GenericAPIView,
    TeamGenericRemovePersonal
):
    serializer_class = TeamProjectManagerSerializer
    queryset = Team.objects.all()

    personal_relation_name = 'project_manager'
    personal_model = ProjectManager

    @response_true_message_schema
    def post(self, request, *args, **kwargs):
        return self._remove_personal(
            request,
            'Project manager for this team removed'
        )
