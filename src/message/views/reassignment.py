from rest_framework import generics

from message.serializers import ReassignmentUpdateSerializer
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
    pass


class ReassignmentDestroyAPIView(
    BaseReassignmentViewGeneric,
    generics.DestroyAPIView
):
    pass


class ReassignmentUpdateAPIView(
    BaseReassignmentViewGeneric,
    generics.UpdateAPIView
):
    serializer_class = ReassignmentUpdateSerializer
