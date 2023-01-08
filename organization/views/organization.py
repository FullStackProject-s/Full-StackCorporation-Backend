from rest_framework import generics

from .generics import OrganizationGenericView


class OrganizationListAPIVIew(
    OrganizationGenericView,
    generics.ListAPIView
):
    pass


class OrganizationRetrieveAPIView(
    OrganizationGenericView,
    generics.RetrieveAPIView
):
    pass


class OrganizationCreateAPIView(
    OrganizationGenericView,
    generics.CreateAPIView
):
    pass


class OrganizationDestroyAPIView(
    OrganizationGenericView,
    generics.DestroyAPIView
):
    pass


class OrganizationUpdateAPIView(
    OrganizationGenericView,
    generics.UpdateAPIView
):
    pass
