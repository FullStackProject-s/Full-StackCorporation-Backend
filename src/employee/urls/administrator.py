from django.urls import path

from employee.views.administrator import (
    AllAdministratorsListAPIView,
    AdministratorCreateAPIView,
    AdministratorDestroyAPIView,
    AdministratorRetrieveAPIView,
    AdministratorUpdateAPIView,
)

urlpatterns_admin = [
    path('all-admins/',
         AllAdministratorsListAPIView.as_view(),
         name='all-admins'
         ),
    path('<int:pk>/',
         AdministratorRetrieveAPIView.as_view(),
         name='admin'
         ),
    path('create-admin/',
         AdministratorCreateAPIView.as_view(),
         name='create-admin'
         ),
    path('delete-admin/<int:pk>/',
         AdministratorDestroyAPIView.as_view(),
         name='delete-admin'
         ),
    path('update-admin/<int:pk>/',
         AdministratorUpdateAPIView.as_view(),
         name='update-admin'
         ),

]