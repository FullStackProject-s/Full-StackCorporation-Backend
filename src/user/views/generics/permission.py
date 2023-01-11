from rest_framework import generics

from user.models import Permissions
from user.serializers import PermissionSerializer


class BaseConfigurationPermissionViewGeneric(generics.GenericAPIView):
    serializer_class = PermissionSerializer
    queryset = Permissions.objects.all()
