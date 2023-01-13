from django.urls import path, include

from .reassignment import urlpatterns_reassignment
from .task import urlpatterns_task

urlpatterns = [
    path('reassignment/', include(urlpatterns_reassignment)),
    path('task/', include(urlpatterns_task)),
]
