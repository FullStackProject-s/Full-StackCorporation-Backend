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
    is_active = models.BooleanField(
        default=True,
        blank=True
    )

    class Meta:
        abstract = True


class OrganizationMessageBase(MessageBase):
    organization = models.ForeignKey(
        'organization.Organization',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        abstract = True
