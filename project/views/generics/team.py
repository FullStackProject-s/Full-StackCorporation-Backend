from drf_spectacular.utils import extend_schema

from rest_framework import generics

from project.models import Team
from project.serializer import (
    TeamSerializer,
    TeamShowSerializer
)


@extend_schema(responses=TeamShowSerializer)
class TeamBaseGenericView(generics.GenericAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
