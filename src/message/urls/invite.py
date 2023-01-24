from django.urls import path
from message.views import invite

urlpatterns_invite = [
    path(
        'all-invites/',
        invite.InviteToOrganizationListAPIVIew.as_view(),
        name='all-invites'
    ),
    path(
        '<int:pk>/',
        invite.InviteToOrganizationRetrieveAPIView.as_view(),
        name='invite'
    ),
    path(
        'invite-create/',
        invite.InviteToOrganizationCreateAPIView.as_view(),
        name='create-invite'
    ),
    path(
        'delete-invite/<int:pk>/',
        invite.InviteToOrganizationDestroyAPIView.as_view(),
        name='delete-invite'
    ),
    path(
        'invite-task/<int:pk>/',
        invite.InviteToOrganizationUpdateAPIView.as_view(),
        name='update-invite'
    ),
]
