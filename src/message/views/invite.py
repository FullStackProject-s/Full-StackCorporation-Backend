from rest_framework import (
    generics,
    permissions
)

from message.serializers import InviteToOrganizationUpdateSerializer
from message.permissions import (
    IsAdministratorOrOwnerOrReadOnlyInvite,
    IsOwnerOrSuperUserMessagePerms
)

from .generic import BaseInviteToOrganizationViewGeneric


class InviteToOrganizationListAPIVIew(
    BaseInviteToOrganizationViewGeneric,
    generics.ListAPIView
):
    pass


class InviteToOrganizationRetrieveAPIView(
    BaseInviteToOrganizationViewGeneric,
    generics.RetrieveAPIView
):
    pass


class InviteToOrganizationCreateAPIView(
    BaseInviteToOrganizationViewGeneric,
    generics.CreateAPIView
):
    pass


class InviteToOrganizationDestroyAPIView(
    BaseInviteToOrganizationViewGeneric,
    generics.DestroyAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrSuperUserMessagePerms
    ]


class InviteToOrganizationUpdateAPIView(
    BaseInviteToOrganizationViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = InviteToOrganizationUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyInvite
    ]
