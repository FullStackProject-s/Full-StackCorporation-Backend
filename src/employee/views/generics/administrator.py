from drf_spectacular.utils import extend_schema
from rest_framework import generics

from employee.models import Administrator
from employee.serializers import (
    AdministratorSerializer,
    AdministratorShowSerializer
)


@extend_schema(responses=AdministratorShowSerializer)
class BaseConfigurationAdministratorsViewGeneric(generics.GenericAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
