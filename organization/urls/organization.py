from django.urls import path
from organization.views.organization import (
    OrganizationListAPIVIew,
    OrganizationRetrieveAPIView,
    OrganizationCreateAPIView,
    OrganizationDestroyAPIView,
    OrganizationUpdateAPIView
)

urlpatterns_organization = [
    path('all-organizations/',
         OrganizationListAPIVIew.as_view(),
         name='all-organizations'
         ),
    path('<int:pk>/',
         OrganizationRetrieveAPIView.as_view(),
         name='organization'
         ),
    path('organization-create/',
         OrganizationCreateAPIView.as_view(),
         name='organization-create'
         ),
    path('delete-organization/<int:pk>/',
         OrganizationDestroyAPIView.as_view(),
         name='delete-organization'
         ),
    path('update-organization/<int:pk>/',
         OrganizationUpdateAPIView.as_view(),
         name='update-organization'
         ),
]
