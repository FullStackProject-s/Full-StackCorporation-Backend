from django.urls import path
from employee.views.specialty import (
    DeveloperOrganizationSpecialtyListAPIView,
    DeveloperOrganizationSpecialtyRetrieveAPIView,
    DeveloperOrganizationSpecialtyDestroyAPIView,
    DeveloperOrganizationSpecialtyCreateAPIView,
    DeveloperOrganizationSpecialtyUpdateAPIView
)

urlpatterns_speciality = [
    path('all-specialities/',
         DeveloperOrganizationSpecialtyListAPIView.as_view(),
         name='all-specialities'
         ),
    path('<int:pk>/',
         DeveloperOrganizationSpecialtyRetrieveAPIView.as_view(),
         name='speciality'
         ),
    path('create-speciality/',
         DeveloperOrganizationSpecialtyCreateAPIView.as_view(),
         name='create-speciality'
         ),
    path('delete-speciality/<int:pk>/',
         DeveloperOrganizationSpecialtyDestroyAPIView.as_view(),
         name='delete-speciality'
         ),
    path('update-speciality/<int:pk>/',
         DeveloperOrganizationSpecialtyUpdateAPIView.as_view(),
         name='update-speciality'
         ),

]
