from drf_spectacular.utils import extend_schema
from rest_framework import generics

from message.serializers import (
    TaskShowSerializer,
    TaskSerializer
)
from message.models import Task


@extend_schema(responses=TaskShowSerializer)
class BaseTaskViewGeneric(generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
