from django.urls import path

from employee.views import administrator

urlpatterns_admin = [
    path(
        'all-admins/',
        administrator.AllAdministratorsListAPIView.as_view(),
        name='all-admins'
    ),
    path(
        '<int:pk>/',
        administrator.AdministratorRetrieveAPIView.as_view(),
        name='admin'
    ),
    path(
        'create-admin/',
        administrator.AdministratorCreateAPIView.as_view(),
        name='create-admin'
    ),
    path(
        'me/',
        administrator.AdministratorMeAPIView.as_view(),
        name='me-admin'
    ),
    path(
        'delete-admin/<int:pk>/',
        administrator.AdministratorDestroyAPIView.as_view(),
        name='delete-admin'
    ),
    path(
        'update-admin/<int:pk>/',
        administrator.AdministratorUpdateAPIView.as_view(),
        name='update-admin'
    ),

]
