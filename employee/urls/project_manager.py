from django.urls import path
from employee.views.project_manager import (
    AllProjectManagerListAPIView,
    ProjectManagerRetrieveAPIView,
    ProjectManagerDestroyAPIView,
    ProjectManagerCreateAPIView,
    ProjectManagerUpdateAPIView
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
         ProjectManagerDestroyAPIView.as_view(),
         name='create-manager'
         ),
    path('delete-manager/<int:pk>/',
         ProjectManagerCreateAPIView.as_view(),
         name='delete-manager'
         ),
    path('update-manager/<int:pk>/',
         ProjectManagerUpdateAPIView.as_view(),
         name='update-manager'
         ),

]
