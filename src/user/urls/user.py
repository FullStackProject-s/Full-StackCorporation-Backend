from django.urls import path
from user.views.user import (
    UserCreateAPIView,
    AllUsersListAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
    UserUpdateAPIView,
)


urlpatterns_user = [
    path('all-users/',
         AllUsersListAPIView.as_view(),
         name='all-users'
         ),
    path('<int:pk>/',
         UserRetrieveAPIView.as_view(),
         name='user'
         ),
    path('delete-user/<int:pk>/',
         UserDestroyAPIView.as_view(),
         name='delete-user'
         ),
    path('create-user/',
         UserCreateAPIView.as_view(),
         name='create-user'
         ),
    path('update-user/<int:pk>/',
         UserUpdateAPIView.as_view(),
         name='update-user',
         ),
]