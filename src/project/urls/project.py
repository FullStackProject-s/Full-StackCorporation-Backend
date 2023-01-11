from django.urls import path
from project.views import project

urlpatterns_project = [
    path(
        'all-projects/',
        project.ProjectsListAPIVIew.as_view(),
        name='all-projects'
    ),
    path(
        '<int:pk>/',
        project.ProjectsRetrieveAPIView.as_view(),
        name='project'
    ),
    path(
        'project-create/',
        project.ProjectCreateAPIView.as_view(),
        name='create-project'
    ),
    path(
        'delete-project/<int:pk>/',
        project.ProjectDestroyAPIView.as_view(),
        name='delete-project'
    ),
    path(
        'update-project/<int:pk>/',
        project.ProjectUpdateAPIView.as_view(),
        name='update-project'
    ),
]
