from django.http import Http404

from rest_framework import (
    generics,
    status
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from general.schema import image_upload_schema
from user.serializers import (
    ProfileImageUploadSerializer,
    ProfileShowSerializer
)
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


class ProfileMeAPIView(
    BaseConfigurationProfilesViewGeneric,
    generics.RetrieveAPIView
):
    def get_object(self):
        if obj := self.get_queryset().filter(user=self.request.user):
            return obj.first()
        raise Http404


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

    @image_upload_schema(ProfileShowSerializer, 'Accept image')
    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if profile.profile_avatar:
            profile.profile_avatar.delete()

        profile.profile_avatar = serializer.validated_data.get(
            'profile_avatar'
        )
        profile.save()

        return Response(
            ProfileShowSerializer(profile).data,
            status=status.HTTP_202_ACCEPTED
        )
