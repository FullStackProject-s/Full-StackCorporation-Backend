from django.urls import path
from message.views import task

urlpatterns_task = [
    path(
        'all-tasks/',
        task.TaskListAPIVIew.as_view(),
        name='all-tasks'
    ),
    path(
        '<int:pk>/',
        task.TaskRetrieveAPIView.as_view(),
        name='task'
    ),
    path(
        'task-create/',
        task.TaskCreateAPIView.as_view(),
        name='create-task'
    ),
    path(
        'delete-task/<int:pk>/',
        task.TaskDestroyAPIView.as_view(),
        name='delete-task'
    ),
    path(
        'update-task/<int:pk>/',
        task.TaskUpdateAPIView.as_view(),
        name='update-task'
    ),
]
