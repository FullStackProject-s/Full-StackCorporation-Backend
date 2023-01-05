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
from general.schemas import response_only_message


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
    ChangePersonalTeamViewMixin
):
    queryset = ProjectManager.objects.all()
    serializer_class = TeamChangeSerializer

    def post(self, request, *args, **kwargs):
        self.serializer_class(data=request.data).is_valid(raise_exception=True)

        return self._post_change_team(
            request,
            f'Team for this project manager now \'{request.data["team"]}\''
        )


class ProjectManagerDeleteTeamAPIView(
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()

    @response_only_message
    def post(self, request, *args, **kwargs):
        return self._post_delete_team("Team for this project manager None")
