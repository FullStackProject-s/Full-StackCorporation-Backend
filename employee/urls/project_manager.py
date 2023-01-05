from django.urls import path
from employee.views.project_manager import (
    AllProjectManagerListAPIView,
    ProjectManagerRetrieveAPIView,
    ProjectManagerDestroyAPIView,
    ProjectManagerCreateAPIView,
    ProjectManagerUpdateAPIView,
    ProjectManagerDeleteTeamAPIView,
    ProjectManagerChangeTeamAPIView
)

urlpatterns_manager = [
    path('all-managers/',
         AllProjectManagerListAPIView.as_view(),
         name='all-managers'
         ),
    path('<int:pk>/',
         ProjectManagerRetrieveAPIView.as_view(),
         name='technology'
         ),
    path('create-manager/',
         ProjectManagerCreateAPIView.as_view(),
         name='create-manager'
         ),
    path('delete-manager/<int:pk>/',
         ProjectManagerDestroyAPIView.as_view(),
         name='delete-manager'
         ),
    path('update-manager/<int:pk>/',
         ProjectManagerUpdateAPIView.as_view(),
         name='update-manager'
         ),
    path('update-manager-team/<int:pk>/',
         ProjectManagerChangeTeamAPIView.as_view(),
         name='update-manager-team',
         ),
    path('delete-manager-team/<int:pk>/',
         ProjectManagerDeleteTeamAPIView.as_view(),
         name='delete-manager-team',
         )

]
