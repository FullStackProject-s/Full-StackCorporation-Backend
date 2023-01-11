from django.db import models
from message.models.message import MessageBase


class Reassignment(MessageBase):
    from_project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='from_project'
    )
    to_project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='to_project'
    )
    from_team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE,
        related_name='from_team'
    )
    to_team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE,
        related_name='to_team'
    )
    confirmed = models.BooleanField(default=False)
