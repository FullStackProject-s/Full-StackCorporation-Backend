from django.urls import path
from user.views import profile

urlpatterns_profile = [
    path(
        'all-profiles/',
        profile.AllProfileListAPIView.as_view(),
        name='all-profiles',
    ),
    path(
        '<int:pk>/',
        profile.ProfileRetrieveAPIView.as_view(),
        name='profile',
    ),
    path(
        'profile-create/',
        profile.ProfileCreateAPIView.as_view(),
        name='create-profile',
    ),
    path(
        'delete-profile/<int:pk>/',
        profile.ProfileDestroyAPIView.as_view(),
        name='delete-profile',
    ),
    path(
        'update-profile/<int:pk>',
        profile.ProfileUpdateAPIView.as_view(),
        name='update-profile',
    ),
    path(
        'upload-image/<int:pk>',
        profile.ProfileImageUploadAPIView.as_view(),
        name='upload-profile-image',
    ),
    path(
        'me/',
        profile.ProfileMeAPIView.as_view(),
        name='me-profile'
    )
]
