from rest_framework import generics

from employee.models import ProjectManager
from employee.serializers import ProjectManagerSerializer


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
