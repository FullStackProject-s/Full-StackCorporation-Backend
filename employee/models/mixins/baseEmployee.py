from django.db import models
from user.models.profile import Profile


class BaseEmployeeMixin(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
