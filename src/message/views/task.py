from rest_framework import generics

from .generic import BaseTaskViewGeneric
from ..serializers import TaskUpdateSerializer


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
    pass


class TaskDestroyAPIView(
    BaseTaskViewGeneric,
    generics.DestroyAPIView
):
    pass


class TaskUpdateAPIView(
    BaseTaskViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = TaskUpdateSerializer
