from django.urls import path
from employee.views import technologies

urlpatterns_techno = [
    path(
        'all-tech/',
        technologies.AllTechnologiesListAPIView.as_view(),
        name='all-tech'
    ),
    path(
        '<int:pk>/',
        technologies.TechnologiesRetrieveAPIView.as_view(),
        name='technology'
    ),
    path(
        'create-tech/',
        technologies.TechnologiesCreateAPIView.as_view(),
        name='create-tech'
    ),
    path(
        'delete-tech/<int:pk>/',
        technologies.TechnologiesDestroyAPIView.as_view(),
        name='delete-tech'
    ),
    path(
        'update-tech/<int:pk>/',
        technologies.TechnologiesUpdateAPIView.as_view(),
        name='update-tech'
    ),

]
