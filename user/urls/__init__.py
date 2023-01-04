from django.urls import path, include

from .user import urlpatterns_user
from .profile import urlpatterns_profile

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('profile/', include(urlpatterns_profile)),
]
