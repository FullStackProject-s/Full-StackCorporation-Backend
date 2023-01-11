from drf_spectacular.utils import extend_schema
from rest_framework import generics

from message.serializers import (
    ReassignmentShowSerializer,
    ReassignmentSerializer
)
from message.models import Reassignment


@extend_schema(responses=ReassignmentShowSerializer)
class BaseReassignmentViewGeneric(generics.GenericAPIView):
    serializer_class = ReassignmentSerializer
    queryset = Reassignment.objects.all()
