from django.db import models

from general.models import TimeStampModelMixin


class Organization(TimeStampModelMixin):
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
    organization_avatar = models.ImageField(blank=True, null=True)
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

    def add_owner(self, owner):
        self.owners.add(owner)
        self.save()
