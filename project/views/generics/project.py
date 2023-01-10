from rest_framework import generics

from drf_spectacular.utils import extend_schema

from project.serializer import (
    ProjectSerializer,
    ProjectShowSerializer
)
from project.models import Project


@extend_schema(responses=ProjectShowSerializer)
class BaseConfigurationProjectsViewGeneric(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
