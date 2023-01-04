from django.urls import path, include

from .team import urlpatterns_team

urlpatterns = [
    path('team/', include(urlpatterns_team)),
]
