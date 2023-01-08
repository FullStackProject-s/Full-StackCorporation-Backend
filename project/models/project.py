from django.db import models
from django.utils import timezone

from general.models import TimeStampModelMixin


class Project(TimeStampModelMixin):
    project_name = models.CharField(
        max_length=200,
        unique=True
    )

    teams = models.ManyToManyField(
        to='project.Team',
        related_name='teams'
    )
    organization = models.ForeignKey(
        'organization.Organization',
        on_delete=models.CASCADE,
        null=True
    )
    deadline = models.DateField(default=timezone.now)
