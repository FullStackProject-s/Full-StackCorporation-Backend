from rest_framework import generics

from employee.models import ProjectManager
from employee.serializers import (
    ProjectManagerSerializer,
    TeamChangeSerializer,
)
from employee.views.service.teamChangeDelete import (
    ChangePersonalTeamViewMixin,
    DeletePersonalTeamViewMixin,
)
from general import (
    ViewsSerializerValidateRequestMixin,
    response_true_message,
    response_true_request_false_message
)


class AllProjectManagerListAPIView(generics.ListAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()


class ProjectManagerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()


class ProjectManagerCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectManagerSerializer


class ProjectManagerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()


class ProjectManagerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()


class ProjectManagerChangeTeamAPIView(
    generics.GenericAPIView,
    ChangePersonalTeamViewMixin,
    ViewsSerializerValidateRequestMixin
):
    queryset = ProjectManager.objects.all()
    serializer_class = TeamChangeSerializer

    @response_true_message
    def post(self, request, *args, **kwargs):
        team_name = self._validate_request(request).data['team']

        return self._post_change_team(
            f'Team for this project manager now \'{team_name}\'',
            team_name
        )


class ProjectManagerDeleteTeamAPIView(
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()

    @response_true_request_false_message
    def post(self, request, *args, **kwargs):
        return self._post_delete_team("Team for this project manager None")
