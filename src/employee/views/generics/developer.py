from drf_spectacular.utils import extend_schema
from rest_framework import generics

from employee.models import Developer
from employee.serializers import (
    DeveloperSerializer,
    DeveloperShowSerializer
)


@extend_schema(responses=DeveloperShowSerializer)
class BaseConfigurationDevelopersViewGeneric(generics.GenericAPIView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
