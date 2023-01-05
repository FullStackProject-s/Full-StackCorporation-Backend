from django.urls import path
from project.views.team import (
    AllTeamListAPIView,
    TeamCreateAPIView,
    TeamChangeNameAPIView,
    TeamRetrieveAPIView,
    TeamUpdateTeamLeadAPIView
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
    path('change-team-name/<int:pk>/',
         TeamChangeNameAPIView.as_view(),
         name='team-change-name',
         ),
    path('team-update-team-lead/<int:pk>/',
         TeamUpdateTeamLeadAPIView.as_view(),
         name='team-update-team-lead'
    )
]
