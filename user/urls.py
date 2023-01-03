from django.urls import path, include
from .views import *

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

urlpatterns_profile = [
    path('all-profiles/',
         AllProfileListAPIView.as_view(),
         name='all-profiles',
         ),
    path('<int:pk>/',
         ProfileRetrieveAPIView.as_view(),
         name='all-profiles',
         ),
    path('profile-create/',
         ProfileCreateAPIView.as_view(),
         name='create-profile',
         ),
    path('delete-profile/<int:pk>/',
         ProfileDestroyAPIView.as_view(),
         name='delete-profile',
         ),
    path('update-profile/<int:pk>',
         ProfileUpdateAPIView.as_view(),
         name='update-profile',
         ),
]
urlpatterns = [

    path('user/', include(urlpatterns_user)),
    path('profile/', include(urlpatterns_profile)),

]
