from rest_framework import (
    generics,
    permissions
)

from message.serializers import CompletedTasksUpdateSerializer
from message.permissions import (
    IsOwnerOrSuperUserMessagePerms,
    IsAdministratorOrOwnerOrReadOnlyReassignment
)
from .generic import BaseCompletedTasksViewGeneric


class CompletedTasksListAPIVIew(
    BaseCompletedTasksViewGeneric,
    generics.ListAPIView
):
    pass


class CompletedTasksRetrieveAPIView(
    BaseCompletedTasksViewGeneric,
    generics.RetrieveAPIView
):
    pass


class CompletedTasksCreateAPIView(
    BaseCompletedTasksViewGeneric,
    generics.CreateAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyReassignment
    ]


class CompletedTasksDestroyAPIView(
    BaseCompletedTasksViewGeneric,
    generics.DestroyAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrSuperUserMessagePerms
    ]


class CompletedTasksUpdateAPIView(
    BaseCompletedTasksViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = CompletedTasksUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyReassignment
    ]
