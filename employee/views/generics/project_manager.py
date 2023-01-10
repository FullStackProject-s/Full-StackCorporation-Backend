from drf_spectacular.utils import extend_schema
from rest_framework import generics

from employee.models import ProjectManager
from employee.serializers import (
    ProjectManagerSerializer,
    ProjectManagerShowSerializer
)


@extend_schema(responses=ProjectManagerShowSerializer)
class BaseConfigurationProjectManagersViewGeneric(generics.GenericAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()
