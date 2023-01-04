from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Team(models.Model):
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
        null=True
    )

    def __str__(self):
        return f'Team name: {self.team_name} - ' \
               f'Team lead: {self.team_lead} - ' \
               f'Prod Manager: {self.project_manager}'
