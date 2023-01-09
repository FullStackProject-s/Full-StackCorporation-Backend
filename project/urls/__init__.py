from django.urls import path, include

from .team import urlpatterns_team
from .project import urlpatterns_project

urlpatterns = [
    path('team/', include(urlpatterns_team)),
    path('project/', include(urlpatterns_project)),
]
