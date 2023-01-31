from django.urls import path, include

from .organization import urlpatterns_organization
from .documents import urlpatterns_document

urlpatterns = [
    path('', include(urlpatterns_organization)),
    path('', include(urlpatterns_document))
]
