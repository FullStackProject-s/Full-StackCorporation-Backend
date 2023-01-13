from rest_framework import generics

from message.serializers import CompletedTasksUpdateSerializer
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
    pass


class CompletedTasksDestroyAPIView(
    BaseCompletedTasksViewGeneric,
    generics.DestroyAPIView
):
    pass


class CompletedTasksUpdateAPIView(
    BaseCompletedTasksViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = CompletedTasksUpdateSerializer
