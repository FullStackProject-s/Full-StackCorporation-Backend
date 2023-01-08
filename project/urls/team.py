from django.urls import path
from project.views.team import (
    AllTeamListAPIView,
    TeamCreateAPIView,
    TeamDestroyAPIView,
    TeamUpdateAPIView,
    TeamRetrieveAPIView,
    TeamUpdateTeamLeadAPIView,
    TeamRemoveTeamLeadAPIView,
    TeamUpdateProjectManagerAPIView,
    TeamRemoveProjectManagerAPIView,
    TeamUpdateDevelopersAPIView,
    TeamRemoveDevelopersAPIView
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
    path('delete-team/<int:pk>/',
         TeamDestroyAPIView.as_view(),
         name='delete-team'
         ),
    path('change-team-name/<int:pk>/',
         TeamUpdateAPIView.as_view(),
         name='team-change-name',
         ),
    path('team-update-team-lead/<int:pk>/',
         TeamUpdateTeamLeadAPIView.as_view(),
         name='team-update-team-lead'
         ),
    path('team-remove-tema-lead/<int:pk>/',
         TeamRemoveTeamLeadAPIView.as_view(),
         name='team-remove-team-lead'
         ),

    path('team-update-project-manager/<int:pk>/',
         TeamUpdateProjectManagerAPIView.as_view(),
         name='team-update-project-manager'
         ),
    path('team-remove-project-manager/<int:pk>/',
         TeamRemoveProjectManagerAPIView.as_view(),
         name='team-remove-project-manager'
         ),
    path('team-update-developers/<int:pk>/',
         TeamUpdateDevelopersAPIView.as_view(),
         name='team-update-developers'
         ),
    path('team-remove-developers/<int:pk>/',
         TeamRemoveDevelopersAPIView.as_view(),
         name='team-remove-developers'
         ),

]
