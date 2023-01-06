from rest_framework import generics

from employee.models import Technologies
from employee.serializers import TechnologiesSerializer


class BaseConfigurationTechnologiesViewGeneric(generics.GenericAPIView):
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
