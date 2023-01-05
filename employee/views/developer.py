from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from employee.models import (
    Developer,
    Technologies
)
from employee.serializers import (
    DeveloperSerializer,
    DeveloperAddStackTechnologiesSerializer
)
from employee.serializers import TeamChangeSerializer
from employee.views.service.teamChangeDelete import (
    ChangePersonalTeamViewMixin,
    DeletePersonalTeamViewMixin
)
from general.services import PostResponse
from general.schemas import (
    response_true_message,
    response_true_request_false_message
)


class AllDeveloperListAPIView(generics.ListAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()


class DeveloperRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()


class DeveloperCreateAPIView(generics.CreateAPIView):
    serializer_class = DeveloperSerializer


class DeveloperDestroyAPIView(generics.DestroyAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()


class DeveloperUpdateAPIView(generics.UpdateAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()


class DeveloperChangeTeamAPIView(
    generics.GenericAPIView,
    ChangePersonalTeamViewMixin
):
    queryset = Developer.objects.all()
    serializer_class = TeamChangeSerializer

    @response_true_message
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        team_name = serializer.data['team']
        return self._post_change_team(
            f'Team for this developer now \'{team_name}\'',
            team_name
        )


class DeveloperDeleteTeamAPIView(
    generics.GenericAPIView,
    DeletePersonalTeamViewMixin
):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()

    @response_true_request_false_message
    def post(self, request, *args, **kwargs):
        return self._post_delete_team('Team for this developer now NULL')


class DeveloperAddStackTechnologies(generics.GenericAPIView):
    serializer_class = DeveloperAddStackTechnologiesSerializer
    queryset = Developer.objects.all()

    def post(self, request, *args, **kwargs):
        dev = self.get_object()

        tech = Technologies.objects.filter(
            technology_name=request.data['technology_name']
        )
        if tech:
            dev.append_technologies([tech.first()])
            return Response(
                DeveloperSerializer(dev).data,
                status=status.HTTP_200_OK
            )
        return PostResponse.not_found_response('Tech not found')


class DeveloperRemoveTechnologies(generics.GenericAPIView):
    serializer_class = DeveloperAddStackTechnologiesSerializer
    queryset = Developer.objects.all()

    def post(self, request, *args, **kwargs):
        dev = self.get_object()

        tech = Technologies.objects.filter(
            technology_name=request.data['technology_name']
        )
        if tech:
            dev.remove_technologies(tech.first())
            return Response(
                DeveloperSerializer(dev).data,
                status=status.HTTP_200_OK
            )
        return PostResponse.not_found_response('Tech not found')
