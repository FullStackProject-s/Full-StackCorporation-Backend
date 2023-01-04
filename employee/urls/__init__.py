from django.urls import path, include

from .technologies import urlpatterns_techno
from .developer import urlpatterns_developers
from .project_manager import urlpatterns_manager
from .administrator import urlpatterns_admin

urlpatterns = [
    path('technologies/', include(urlpatterns_techno)),
    path('developers/', include(urlpatterns_developers)),
    path('project-manager/', include(urlpatterns_manager)),
    path('admin/', include(urlpatterns_admin))

]