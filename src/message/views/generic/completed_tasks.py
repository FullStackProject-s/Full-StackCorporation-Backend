from drf_spectacular.utils import extend_schema
from rest_framework import generics

from message.serializers import (
    CompletedTasksSerializer,
    CompletedTasksShowSerializer
)
from message.models import CompletedTasks


@extend_schema(responses=CompletedTasksShowSerializer)
class BaseCompletedTasksViewGeneric(generics.GenericAPIView):
    serializer_class = CompletedTasksSerializer
    queryset = CompletedTasks.objects.all()
