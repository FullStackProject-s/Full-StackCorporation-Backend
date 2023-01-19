from django.utils.translation import gettext_lazy as _
from django.db import models


class InviteStatus(models.TextChoices):
    CONFIRMED = 'Confirmed', _('Confirmed')
    WAITING = 'Waiting', _('Waiting')
    REJECTED = 'Rejected', _('Rejected')
