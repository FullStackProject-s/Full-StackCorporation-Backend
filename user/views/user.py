from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import (
    CustomUserSerializer,
    CustomUserCreateSerializer
)

User = get_user_model()


class AllUsersListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
