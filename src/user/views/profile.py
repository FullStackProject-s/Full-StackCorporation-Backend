from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from user.serializers import ProfileImageUploadSerializer, \
    ProfileShowSerializer
from user.views.generics import BaseConfigurationProfilesViewGeneric


class AllProfileListAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.ListAPIView
):
    pass


class ProfileRetrieveAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.RetrieveAPIView
):
    pass


class ProfileCreateAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.CreateAPIView
):
    pass


class ProfileDestroyAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.DestroyAPIView
):
    pass


class ProfileUpdateAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.UpdateAPIView
):
    pass


class ProfileImageUploadAPIView(BaseConfigurationProfilesViewGeneric):
    serializer_class = ProfileImageUploadSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        if profile.profile_avatar:
            profile.profile_avatar.delete()
            profile.save()
        profile.profile_avatar = serializer.validated_data.get(
            'profile_avatar')
        profile.save()
        return Response(
            ProfileShowSerializer(profile).data,
            status=status.HTTP_200_OK
        )
