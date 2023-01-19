from django.urls import path
from project.views import team

urlpatterns_team = [
    path(
        'all-teams/',
        team.AllTeamListAPIView.as_view(),
        name='all-teams'
    ),
    path(
        '<int:pk>',
        team.TeamRetrieveAPIView.as_view(),
        name='team'
    ),
    path(
        'team-create/',
        team.TeamCreateAPIView.as_view(),
        name='create-team'
    ),
    path(
        'delete-team/<int:pk>/',
        team.TeamDestroyAPIView.as_view(),
        name='delete-team'
    ),
    path(
        'update-team/<int:pk>/',
        team.TeamUpdateAPIView.as_view(),
        name='update-team',
    ),

]
