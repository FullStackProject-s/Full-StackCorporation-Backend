from django.urls import path
from user.views.profile import (
    AllProfileListAPIView,
    ProfileRetrieveAPIView,
    ProfileCreateAPIView,
    ProfileDestroyAPIView,
    ProfileUpdateAPIView
)

urlpatterns_profile = [
    path('all-profiles/',
         AllProfileListAPIView.as_view(),
         name='all-profiles',
         ),
    path('<int:pk>/',
         ProfileRetrieveAPIView.as_view(),
         name='profile',
         ),
    path('profile-create/',
         ProfileCreateAPIView.as_view(),
         name='create-profile',
         ),
    path('delete-profile/<int:pk>/',
         ProfileDestroyAPIView.as_view(),
         name='delete-profile',
         ),
]
