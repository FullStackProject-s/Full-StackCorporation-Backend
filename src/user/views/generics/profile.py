from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.models import Profile
from user.serializers import (
    ProfileSerializer,
    ProfileShowSerializer
)
from user.permissions import IsOwnerOrReadOnlyProfile


@extend_schema(responses=ProfileShowSerializer)
class BaseConfigurationProfilesViewGeneric(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyProfile]
