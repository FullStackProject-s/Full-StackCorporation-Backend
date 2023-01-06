from rest_framework import generics

from user.models import Profile
from user.serializers import ProfileSerializer


class BaseConfigurationProfilesViewGeneric(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
