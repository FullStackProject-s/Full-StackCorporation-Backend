from general.models import BaseTimeStampModel
from django.db import models


class MessageBase(BaseTimeStampModel):
    creator = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        max_length=10_000,

    )

    class Meta:
        abstract = True
