from django.utils.translation import gettext_lazy as _

from django.db import models


class Specialty(models.TextChoices):
    FRONT = 'Front', _('Frontend')
    BACK = 'Back', _('Backend')
    DEVOPS = 'DevOps', _('Development & Operations')


class TechnologiesStack(models.TextChoices):
    FRONT = 'Front', _('Frontend')
    BACK = 'Back', _('Backend')
    DEVOPS = 'DevOps', _('Development & Operations')
    GEN_TECH = 'Gen tech', _('General technologies')
