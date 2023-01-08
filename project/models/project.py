from django.db import models
from django.utils import timezone

from general.models import TimeStampModelMixin


class Project(TimeStampModelMixin):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    teams = models.ManyToManyField(
        to='project.Team',
        related_name='teams'
    )
    deadline = models.DateField(default=timezone.now)
