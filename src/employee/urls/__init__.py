from django.urls import path, include

from .technologies import urlpatterns_techno
from .developer import urlpatterns_developers
from .project_manager import urlpatterns_manager
from .administrator import urlpatterns_admin
from .specialty import urlpatterns_speciality

urlpatterns = [
    path('technologies/', include(urlpatterns_techno)),
    path('developer/', include(urlpatterns_developers)),
    path('project-manager/', include(urlpatterns_manager)),
    path('administrator/', include(urlpatterns_admin)),
    path('speciality/', include(urlpatterns_speciality))

]
