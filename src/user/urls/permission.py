from django.urls import path
from user.views import permission

urlpatterns_permission = [
    path(
        'all-permissions/',
        permission.AllPermissionListAPIView.as_view(),
        name='all-permissions'
    ),
    path(
        '<int:pk>/',
        permission.PermissionRetrieveAPIView.as_view(),
        name='permission'
    ),
    path(
        'create-permission/',
        permission.PermissionCreateAPIView.as_view(),
        name='create-permission'
    ),
    path(
        'delete-permission/<int:pk>/',
        permission.PermissionDestroyAPIView.as_view(),
        name='delete-permission'
    ),
]
