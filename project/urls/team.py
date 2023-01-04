from django.urls import path
from project.views.team import (
    AllTeamListAPIView,
    TeamCreateAPIView,
    TeamChangeNameAPIView,
    TeamRetrieveAPIView,
)

urlpatterns_team = [
    path('all-team/',
         AllTeamListAPIView.as_view(),
         name='all-teams'
         ),
    path('<int:pk>',
         TeamRetrieveAPIView.as_view(),
         name='team'
         ),
    path('team-create/',
         TeamCreateAPIView.as_view(),
         name='create-team'
         ),
    path('team-change-name/<int:pk>/',
         TeamChangeNameAPIView.as_view(),
         name='team-change-name',
         )
]
