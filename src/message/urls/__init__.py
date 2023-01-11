from django.urls import path, include

from .reassignment import urlpatterns_reassignment

urlpatterns = [
    path('reassignment/', include(urlpatterns_reassignment)),
]
