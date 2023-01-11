from message.models.message import MessageBase
from django.db import models


class Task(MessageBase):
    pass


class CompletedTasks(MessageBase):
    checked = models.BooleanField(default=False)
    task = models.ManyToManyField(
        Task,
        related_name='task'
    )
