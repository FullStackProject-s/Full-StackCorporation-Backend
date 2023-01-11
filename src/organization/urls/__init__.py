from django.urls import path, include

from .organization import urlpatterns_organization


urlpatterns = [
    path('organization/', include(urlpatterns_organization)),
]
