from rest_framework import generics

from employee.models import ProjectManager
from employee.serializers import ProjectManagerSerializer
from employee.views.schemas import change_team, delete_team
from employee.views.service.developer_post import DeveloperPostResponse
from employee.views.service.teamChangeDelete import \
    ChangePersonalTeamViewMixin, DeletePersonalTeamViewMixin

from project.models import Team


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
    serializer_class = ProjectManagerSerializer

    @change_team
    def post(self, request, *args, **kwargs):
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

    @delete_team
    def post(self, request, *args, **kwargs):
        return self._post_delete_team("Team for this project manager None")
