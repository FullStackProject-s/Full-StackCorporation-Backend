from drf_spectacular.utils import extend_schema, extend_schema_view

from user.models.profile import Profile
from rest_framework import generics
from user.serializers.profile import ProfileSerializer


class AllProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfileSerializer


class ProfileDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
