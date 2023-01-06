from rest_framework import generics

from employee.models import Developer
from employee.serializers import DeveloperSerializer


class BaseConfigurationDevelopersViewGeneric(generics.GenericAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
