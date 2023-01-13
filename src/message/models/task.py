from django.db import models
from message.models.generic import MessageBase


class Task(MessageBase):
    pass


class CompletedTasks(MessageBase):
    checked = models.BooleanField(default=False)
    task = models.ManyToManyField(
        Task,
        related_name='task'
    )
