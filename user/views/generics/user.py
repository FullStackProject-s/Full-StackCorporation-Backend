from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import CustomUserSerializer

User = get_user_model()


class BaseConfigurationUsersViewGeneric(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
