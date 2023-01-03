from django.db import models


class Team(models.Model):
    team_name = models.CharField(
        max_length=200,
        unique=True
    )
    team_lead = models.ForeignKey(
        'employee.Developer',
        on_delete=models.CASCADE,
        related_name='team_lead'
    )
    project_manager = models.ForeignKey(
        'employee.ProjectManager',
        on_delete=models.CASCADE,
        related_name='project_manager'
    )
    developers = models.ManyToManyField(
        'employee.Developer',
        related_name='developers'
    )
