from django.urls import path
from message.views import reassignment

urlpatterns_reassignment = [
    path(
        'all-reassignments/',
        reassignment.ReassignmentListAPIVIew.as_view(),
        name='all-reassignments'
    ),
    path(
        '<int:pk>/',
        reassignment.ReassignmentRetrieveAPIView.as_view(),
        name='reassignment'
    ),
    path(
        'reassignment-create/',
        reassignment.ReassignmentCreateAPIView.as_view(),
        name='create-reassignment'
    ),
    path(
        'delete-reassignment/<int:pk>/',
        reassignment.ReassignmentDestroyAPIView.as_view(),
        name='delete-reassignment'
    ),
    path(
        'update-reassignment/<int:pk>/',
        reassignment.ReassignmentUpdateAPIView.as_view(),
        name='update-reassignment'
    ),
]
