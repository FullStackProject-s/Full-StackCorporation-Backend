from rest_framework import (
    generics,
    permissions
)

from .generic import BaseTaskViewGeneric

from message.permissions import IsAdministratorOrOwnerOrReadOnlyTask
from message.serializers import TaskUpdateSerializer


class TaskListAPIVIew(
    BaseTaskViewGeneric,
    generics.ListAPIView
):
    pass


class TaskRetrieveAPIView(
    BaseTaskViewGeneric,
    generics.RetrieveAPIView
):
    pass


class TaskCreateAPIView(
    BaseTaskViewGeneric,
    generics.CreateAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyTask
    ]


class TaskDestroyAPIView(
    BaseTaskViewGeneric,
    generics.DestroyAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyTask
    ]


class TaskUpdateAPIView(
    BaseTaskViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = TaskUpdateSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdministratorOrOwnerOrReadOnlyTask
    ]
