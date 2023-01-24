from django.db import models
from message.models.generic import OrganizationMessageBase


class Task(OrganizationMessageBase):
    completed = models.BooleanField(default=False)


class CompletedTasks(OrganizationMessageBase):
    checked = models.BooleanField(default=False)
    tasks = models.ManyToManyField(
        Task,
        related_name='task'
    )
