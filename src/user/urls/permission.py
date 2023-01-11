from django.urls import path
from user.views.permission import (
    AllPermissionListAPIView,
    PermissionRetrieveAPIView,
    PermissionCreateAPIView,
    PermissionDestroyAPIView,
)

urlpatterns_permission = [
    path('all-permissions/',
         AllPermissionListAPIView.as_view(),
         name='all-permissions'
         ),
    path('<int:pk>/',
         PermissionRetrieveAPIView.as_view(),
         name='permission'
         ),
    path('create-permission/',
         PermissionCreateAPIView.as_view(),
         name='create-permission'
         ),
    path('delete-permission/<int:pk>/',
         PermissionDestroyAPIView.as_view(),
         name='delete-permission'
         ),
]
