from django.urls import path
from employee.views.developer import (
    AllDeveloperListAPIView,
    DeveloperRetrieveAPIView,
    DeveloperDestroyAPIView,
    DeveloperCreateAPIView,
    DeveloperUpdateAPIView,
    DeveloperChangeTeamAPIView
)

urlpatterns_developers = [
    path('all-developers/',
         AllDeveloperListAPIView.as_view(),
         name='all-developers'
         ),
    path('<int:pk>/',
         DeveloperRetrieveAPIView.as_view(),
         name='developer'
         ),
    path('create-developer/',
         DeveloperCreateAPIView.as_view(),
         name='create-developer'
         ),
    path('delete-developer/<int:pk>/',
         DeveloperDestroyAPIView.as_view(),
         name='delete-developer'
         ),
    path('update-developer/<int:pk>/',
         DeveloperUpdateAPIView.as_view(),
         name='update-developer'
         ),
    path('update-developer-team/<int:pk>/',
         DeveloperChangeTeamAPIView.as_view(),
         name='update-developer-team'
         ),

]
