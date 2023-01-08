from django.db import models
from django.utils import timezone

from general.models import TimeStampModelMixin


class Team(TimeStampModelMixin):
    team_name = models.CharField(
        max_length=200,
        unique=True
    )
    team_lead = models.ForeignKey(
        'employee.Developer',
        on_delete=models.CASCADE,
        related_name='team_lead',
        blank=True,
        null=True
    )
    project_manager = models.ForeignKey(
        'employee.ProjectManager',
        on_delete=models.CASCADE,
        related_name='project_manager',
        blank=True,
        null=True
    )
    developers = models.ManyToManyField(
        'employee.Developer',
        related_name='developers',
        blank=True,
    )

    def append_developer(self, developer):
        self.developers.add(developer)
        self.save()

    def remove_developer(self, developer):
        self.developers.remove(developer)
        self.save()

    def __str__(self):
        return f'Team name: {self.team_name} - ' \
               f'Team lead: {self.team_lead} - ' \
               f'Prod Manager: {self.project_manager} - ' \
               f'pk : {self.pk}'


