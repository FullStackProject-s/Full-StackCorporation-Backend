from django.urls import (
    path,
    include
)

from .utils import filtered_djoser_urls
from .token import urlpatterns_token
from .djoser import urlpatterns_djoser

urlpatterns = [
    path('token/', include(urlpatterns_token)),
    path('', include(filtered_djoser_urls(urlpatterns_djoser))),
]
