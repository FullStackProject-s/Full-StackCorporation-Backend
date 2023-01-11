from django.urls import path
from project.views.team import (
    AllTeamListAPIView,
    TeamCreateAPIView,
    TeamDestroyAPIView,
    TeamUpdateAPIView,
    TeamRetrieveAPIView
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
    path('update-team/<int:pk>/',
         TeamUpdateAPIView.as_view(),
         name='update-team',
         ),

]
