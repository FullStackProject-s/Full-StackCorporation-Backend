from django.db import models

from general.models import BaseTimeStampModel


class Organization(BaseTimeStampModel):
    organization_name = models.CharField(
        max_length=200,
        unique=True,
    )
    owner = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.CASCADE,
        related_name='org_owner',
        null=True
    )
    organization_avatar = models.ImageField(
        upload_to='organization_avatar',
        blank=True,
        null=True
    )
    projects = models.ManyToManyField(
        'project.Project',
        related_name='org_projects',
        blank=True
    )
    members = models.ManyToManyField(
        'user.CustomUser',
        related_name='org_members',
        blank=True
    )

    def __str__(self):
        return f'{self.organization_name} - {self.pk}'
