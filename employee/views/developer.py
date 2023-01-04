from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from employee.models import (
    Developer,
    Technologies
)
from employee.serializers import (
    DeveloperSerializer,
    DeveloperChangeTeamSerializer,
    DeveloperAddStackTechnologiesSerializer
)
from employee.views.service.developer_post import DeveloperPostNotFound
from project.models.team import Team


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


class DeveloperChangeTeamAPIView(generics.UpdateAPIView):
    serializer_class = DeveloperChangeTeamSerializer
    queryset = Developer.objects.all()

    def post(self, request, *args, **kwargs):

        dev = self.get_object()

        if x := Team.objects.filter(team_name=request.data['team']):
            dev.team = x.first()
            dev.save()
            return Response(
                DeveloperSerializer(dev).data,
                status=status.HTTP_200_OK
            )
        if request.data['team'] == '':
            dev.team = None
            dev.save()
            return Response(
                {
                    "message": "Team from this developer NULL."
                },
                status=status.HTTP_200_OK
            )
        return DeveloperPostNotFound.not_found_response('Team not found')


class DeveloperAddStackTechnologies(generics.GenericAPIView):
    serializer_class = DeveloperAddStackTechnologiesSerializer

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
        return DeveloperPostNotFound.not_found_response('Tech not found')


class DeveloperRemoveTechnologies(generics.GenericAPIView):
    serializer_class = DeveloperAddStackTechnologiesSerializer

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
        return DeveloperPostNotFound.not_found_response('Tech not found')

