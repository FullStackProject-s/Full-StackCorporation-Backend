from django.urls import path
from organization.views import organization

urlpatterns_organization = [
    path(
        'all-organizations/',
        organization.OrganizationListAPIVIew.as_view(),
        name='all-organizations'
    ),
    path(
        '<int:pk>/',
        organization.OrganizationRetrieveAPIView.as_view(),
        name='organization'
    ),
    path(
        'organization-create/',
        organization.OrganizationCreateAPIView.as_view(),
        name='organization-create'
    ),
    path(
        'delete-organization/<int:pk>/',
        organization.OrganizationDestroyAPIView.as_view(),
        name='delete-organization'
    ),
    path(
        'update-organization/<int:pk>/',
        organization.OrganizationUpdateAPIView.as_view(),
        name='update-organization'
    ),
]
