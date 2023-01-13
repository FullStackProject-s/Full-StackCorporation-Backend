from django.urls import path
from message.views import completed_tasks

urlpatterns_completed_tasks = [
    path(
        'all-completed-tasks/',
        completed_tasks.CompletedTasksListAPIVIew.as_view(),
        name='all-completed-tasks'
    ),
    path(
        '<int:pk>/',
        completed_tasks.CompletedTasksRetrieveAPIView.as_view(),
        name='completed-tasks'
    ),
    path(
        'completed-tasks-create/',
        completed_tasks.CompletedTasksCreateAPIView.as_view(),
        name='create-completed-tasks'
    ),
    path(
        'delete-completed-tasks/<int:pk>/',
        completed_tasks.CompletedTasksDestroyAPIView.as_view(),
        name='delete-completed-tasks'
    ),
    path(
        'update-completed-tasks/<int:pk>/',
        completed_tasks.CompletedTasksUpdateAPIView.as_view(),
        name='update-completed-tasks'
    ),
]
