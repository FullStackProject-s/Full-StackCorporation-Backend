from django.urls import path
from project.views.project import (
    ProjectsListAPIVIew,
    ProjectsRetrieveAPIView,
    ProjectCreateAPIView,
    ProjectDestroyAPIView,
    ProjectUpdateAPIView
)

urlpatterns_project = [
    path('all-projects/',
         ProjectsListAPIVIew.as_view(),
         name='all-projects'
         ),
    path('<int:pk>/',
         ProjectsRetrieveAPIView.as_view(),
         name='project'
         ),
    path('project-create/',
         ProjectCreateAPIView.as_view(),
         name='create-project'
         ),
    path('delete-project/<int:pk>/',
         ProjectDestroyAPIView.as_view(),
         name='delete-project'
         ),
    path('update-project/<int:pk>/',
         ProjectUpdateAPIView.as_view(),
         name='update-project'
         ),
]
