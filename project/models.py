from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(
        max_length=200,
        unique=True
    )
    team_lead = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE
    )
    project_manager = models.ForeignKey(
        ProjectManager,
        on_delete=models.CASCADE
    )
    developers = models.ManyToManyField(Developer)
