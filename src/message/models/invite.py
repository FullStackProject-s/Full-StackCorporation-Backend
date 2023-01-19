from django.db import models

from message.models.generic import MessageBase
from message.models.consts import InviteStatus


class InviteToOrganization(MessageBase):
    to_organization = models.ForeignKey(
        'organization.Organization',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=200,
        choices=InviteStatus.choices,
        default=InviteStatus.WAITING
    )
