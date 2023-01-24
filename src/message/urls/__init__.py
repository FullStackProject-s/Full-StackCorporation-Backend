from django.urls import path, include

from .reassignment import urlpatterns_reassignment
from .task import urlpatterns_task
from .completed_tasks import urlpatterns_completed_tasks
from .invite import urlpatterns_invite

urlpatterns = [
    path('reassignment/', include(urlpatterns_reassignment)),
    path('task/', include(urlpatterns_task)),
    path('completed-tasks/', include(urlpatterns_completed_tasks)),
    path('invite/', include(urlpatterns_invite))
]
