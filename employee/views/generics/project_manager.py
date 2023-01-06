from rest_framework import generics

from employee.models import ProjectManager
from employee.serializers import ProjectManagerSerializer


class BaseConfigurationProjectManagersViewGeneric(generics.GenericAPIView):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()
