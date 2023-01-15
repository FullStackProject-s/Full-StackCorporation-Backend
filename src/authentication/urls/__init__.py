from django.urls import (
    path,
    include
)

from .token import urlpatterns_token
from djoser.urls import urlpatterns as urls

# print(urls)
urlpatterns = [
    path('', include(urlpatterns_token)),
    path('', include('djoser.urls'))

]
