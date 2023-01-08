from django.db import models
from message.models.message import MessageBase


class Reassignment(MessageBase):
    from_project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE
    )
    to_project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE
    )
    from_team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE
    )
    to_team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE
    )
    confirmed = models.BooleanField(default=False)
