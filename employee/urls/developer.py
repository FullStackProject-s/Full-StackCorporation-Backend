from django.urls import path
from employee.views.developer import (
    AllDeveloperListAPIView,
    DeveloperRetrieveAPIView,
    DeveloperDestroyAPIView,
    DeveloperCreateAPIView,
    DeveloperUpdateAPIView,
    DeveloperAddStackTechnologies,
    DeveloperRemoveTechnologies,
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
    path('add-developer-tech/<int:pk>/',
         DeveloperAddStackTechnologies.as_view(),
         name='add-developer-tech'
         ),
    path('remove-developer-tech/<int:pk>/',
         DeveloperRemoveTechnologies.as_view(),
         name='remove-developer-tech'
         )

]
