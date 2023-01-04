from django.urls import path
from project.views.team import (
    AllTeamListAPIView,
    TeamCreateAPIView,
)

urlpatterns_team = [
    path('all-team/',
         AllTeamListAPIView.as_view(),
         name='all-developers'
         ),
    path('team-create/',
         TeamCreateAPIView.as_view(),
         name='create-team'
         )
]
