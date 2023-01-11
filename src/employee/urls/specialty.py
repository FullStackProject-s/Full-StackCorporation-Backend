from django.urls import path
from employee.views import specialty

urlpatterns_speciality = [
    path(
        'all-specialities/',
        specialty.DeveloperOrganizationSpecialtyListAPIView.as_view(),
        name='all-specialities'
    ),
    path(
        '<int:pk>/',
        specialty.DeveloperOrganizationSpecialtyRetrieveAPIView.as_view(),
        name='speciality'
    ),
    path(
        'create-speciality/',
        specialty.DeveloperOrganizationSpecialtyCreateAPIView.as_view(),
        name='create-speciality'
    ),
    path(
        'delete-speciality/<int:pk>/',
        specialty.DeveloperOrganizationSpecialtyDestroyAPIView.as_view(),
        name='delete-speciality'
    ),
    path(
        'update-speciality/<int:pk>/',
        specialty.DeveloperOrganizationSpecialtyUpdateAPIView.as_view(),
        name='update-speciality'
    ),

]
