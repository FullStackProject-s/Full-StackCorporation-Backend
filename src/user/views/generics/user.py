from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.permissions import IsOwnerOrReadOnlyCustomUser
from user.serializers import (
    CustomUserSerializer,
    CustomUserShowSerializer,
)

User = get_user_model()


@extend_schema(responses=CustomUserShowSerializer)
class BaseConfigurationUsersViewGeneric(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyCustomUser]
