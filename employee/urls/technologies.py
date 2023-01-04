from django.urls import path
from employee.views.technologies import (
    AllTechnologiesListAPIView,
    TechnologiesRetrieveAPIView,
    TechnologiesDestroyAPIView,
    TechnologiesCreateAPIView,
    TechnologiesUpdateAPIView
)

urlpatterns_techno = [
    path('all-tech/',
         AllTechnologiesListAPIView.as_view(),
         name='all-tech'
         ),
    path('<int:pk>/',
         TechnologiesRetrieveAPIView.as_view(),
         name='technology'
         ),
    path('create-tech/',
         TechnologiesCreateAPIView.as_view(),
         name='create-tech'
         ),
    path('delete-tech/<int:pk>/',
         TechnologiesDestroyAPIView.as_view(),
         name='delete-tech'
         ),
    path('update-tech/<int:pk>/',
         TechnologiesUpdateAPIView.as_view(),
         name='update-tech'
         ),

]
