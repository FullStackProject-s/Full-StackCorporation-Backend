from rest_framework import (
    generics,
    permissions
)

from message.serializers import ReassignmentUpdateSerializer
from message.permissions import (
    IsOwnerOrSuperUserMessagePerms,
    IsAdministratorOrOwnerOrReadOnlyReassignment
)
from .generic import BaseReassignmentViewGeneric


class ReassignmentListAPIVIew(
    BaseReassignmentViewGeneric,
    generics.ListAPIView
):
    pass


class ReassignmentRetrieveAPIView(
    BaseReassignmentViewGeneric,
    generics.RetrieveAPIView
):
    pass


class ReassignmentCreateAPIView(
    BaseReassignmentViewGeneric,
    generics.CreateAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyReassignment
    ]


class ReassignmentDestroyAPIView(
    BaseReassignmentViewGeneric,
    generics.DestroyAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrSuperUserMessagePerms
    ]


class ReassignmentUpdateAPIView(
    BaseReassignmentViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = ReassignmentUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyReassignment
    ]
