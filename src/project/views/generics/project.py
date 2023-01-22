from rest_framework import (
    generics,
    permissions
)

from drf_spectacular.utils import extend_schema

from project.permissions import IsAdministratorOrOwnerOrReadOnlyProject
from project.serializer import (
    ProjectSerializer,
    ProjectShowSerializer
)
from project.models import Project


@extend_schema(responses=ProjectShowSerializer)
class BaseConfigurationProjectsViewGeneric(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyProject
    ]
