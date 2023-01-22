from django.urls import path
from employee.views import project_manager

urlpatterns_manager = [
    path(
        'all-managers/',
        project_manager.AllProjectManagerListAPIView.as_view(),
        name='all-managers'
    ),
    path(
        '<int:pk>/',
        project_manager.ProjectManagerRetrieveAPIView.as_view(),
        name='project-manager'
    ),
    path(
        'me/',
        project_manager.ProjectManagerAPIView.as_view(),
        name='me-project-manager'
    ),
    path(
        'create-manager/',
        project_manager.ProjectManagerCreateAPIView.as_view(),
        name='create-manager'
    ),
    path(
        'delete-manager/<int:pk>/',
        project_manager.ProjectManagerDestroyAPIView.as_view(),
        name='delete-manager'
    ),
    path(
        'update-manager/<int:pk>/',
        project_manager.ProjectManagerUpdateAPIView.as_view(),
        name='update-manager'
    ),
]
