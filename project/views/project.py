from rest_framework import generics
from project.models import Project
from project.serializer import ProjectSerializer


class ProjectsListAPIVIew(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


