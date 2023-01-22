from rest_framework import (
    generics,
    permissions
)

from drf_spectacular.utils import extend_schema

from project.models import Team
from project.permissions.team import (
    IsProjectManagerOrAdministratorOrOwnerOrReadOnlyTeam
)
from project.serializer import (
    TeamSerializer,
    TeamShowSerializer
)


@extend_schema(responses=TeamShowSerializer)
class TeamBaseGenericView(generics.GenericAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsProjectManagerOrAdministratorOrOwnerOrReadOnlyTeam
    ]
