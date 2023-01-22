from django.db import models

from general.models import BaseTimeStampModel


class Project(BaseTimeStampModel):
    project_name = models.CharField(
        max_length=200,
        unique=True
    )

    teams = models.ManyToManyField(
        to='project.Team',
        related_name='teams',
        blank=True
    )
    organization = models.ForeignKey(
        'organization.Organization',
        on_delete=models.CASCADE,
    )
    deadline = models.DateField(blank=False)

    def set_organization(self, organization):
        self.organization = organization
        self.save()

    def remove_organization(self):
        self.organization = None
        self.save()
