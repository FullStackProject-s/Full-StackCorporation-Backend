from django.db import models

from general.models import BaseTimeStampModel


class Team(BaseTimeStampModel):
    team_name = models.CharField(
        max_length=200,
        unique=True
    )
    team_lead = models.ForeignKey(
        'employee.Developer',
        on_delete=models.SET_NULL,
        related_name='team_lead',
        blank=True,
        null=True
    )
    project_manager = models.ForeignKey(
        'employee.ProjectManager',
        related_name='project_manager',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    developers = models.ManyToManyField(
        'employee.Developer',
        related_name='developers',
        blank=True,
    )

    def __str__(self):
        return f'Team name: {self.team_name} - ' \
               f'Team lead: {self.team_lead} - ' \
               f'Prod Manager: {self.project_manager} - ' \
               f'pk : {self.pk}'
