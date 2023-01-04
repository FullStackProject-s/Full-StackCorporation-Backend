from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from employee.models.employees import Developer
from employee.serializers.developer import (
    DeveloperSerializer,
    DeveloperSerializerChangeTeam
)
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
    serializer_class = DeveloperSerializerChangeTeam
    queryset = Developer.objects.all()

    def update(self, request, *args, **kwargs):
        dev = Developer.objects.get(pk=kwargs.pop('pk'))
        if x := Team.objects.filter(team_name=request.data['team']):
            dev.team = x.first()
            dev.save()
            return Response(
                DeveloperSerializer(dev).data,
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "This team name is invalid"},
            status=status.HTTP_400_BAD_REQUEST
        )
#
# class DeveloperUpdate