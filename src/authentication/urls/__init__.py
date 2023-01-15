from django.urls import (
    path,
    include
)
from .token import urlpatterns_token

urlpatterns = [
    path('', include(urlpatterns_token))
]
