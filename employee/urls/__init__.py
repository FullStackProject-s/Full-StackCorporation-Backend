from django.urls import path, include

from .technologies import urlpatterns_techno
from .developer import urlpatterns_developers
urlpatterns = [
    path('technologies/', include(urlpatterns_techno)),
    path('developers/', include(urlpatterns_developers)),
]
