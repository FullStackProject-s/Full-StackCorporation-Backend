from django.urls import path
from employee.views import developer

urlpatterns_developers = [
    path(
        'all-developers/',
        developer.AllDeveloperListAPIView.as_view(),
        name='all-developers'
    ),
    path(
        '<int:pk>/',
        developer.DeveloperRetrieveAPIView.as_view(),
        name='developer'
    ),
    path(
        'me/',
        developer.DeveloperMeAPIView.as_view(),
        name='me-developer'
    ),
    path(
        'create-developer/',
        developer.DeveloperCreateAPIView.as_view(),
        name='create-developer'
    ),
    path(
        'delete-developer/<int:pk>/',
        developer.DeveloperDestroyAPIView.as_view(),
        name='delete-developer'
    ),
    path(
        'update-developer/<int:pk>/',
        developer.DeveloperUpdateAPIView.as_view(),
        name='update-developer'
    ),

]
