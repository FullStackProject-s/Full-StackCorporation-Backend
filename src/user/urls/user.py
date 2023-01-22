from django.urls import path
from user.views import user

urlpatterns_user = [
    path(
        'all-users/',
        user.AllUsersListAPIView.as_view(),
        name='all-users'
    ),
    path(
        '<int:pk>/',
        user.UserRetrieveAPIView.as_view(),
        name='user'
    ),
    path(
        'me/',
        user.UserMeAPIView.as_view(),
        name='me-user'
    ),
    path(
        'delete-user/<int:pk>/',
        user.UserDestroyAPIView.as_view(),
        name='delete-user'
    ),
    path(
        'update-user/<int:pk>/',
        user.UserUpdateAPIView.as_view(),
        name='update-user',
    ),

]
