from django.db import models

from general.models import TimeStampModelMixin


class Organization(TimeStampModelMixin):
    organization_name = models.CharField(
        max_length=200,
        unique=True,
    )
    owners = models.ManyToManyField(
        'user.CustomUser',
        related_name='org_owners'
    )
    projects = models.ManyToManyField(
        'project.Project',
        related_name='org_projects'
    )
    members = models.ManyToManyField(
        'user.CustomUser',
        related_name='org_members'
    )
