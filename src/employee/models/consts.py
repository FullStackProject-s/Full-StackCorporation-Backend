from django.utils.translation import gettext_lazy as _

from django.db import models


class Specialty(models.TextChoices):
    FRONT = 'Frontend', _('Frontend')
    BACK = 'Backend', _('Backend')
    FULLSTACK = 'Full-Stack', _('Full-Stack')
    DEVOPS = 'Development & Operations', _('Development & Operations')


class SkillLevel(models.TextChoices):
    junior = 'Junior', _('Junior')
    junior_plus = 'Junior Plus', _('Junior Plus')
    middle = 'Middle', _('Middle')
    middle_plus = 'Middle Plus', _('Middle Plus')
    senior = 'Senior', _('Senior')


class TechnologiesStack(models.TextChoices):
    FRONT = 'Frontend', _('Frontend')
    BACK = 'Backend', _('Backend')
    DEVOPS = 'Development & Operations', _('Development & Operations')
    GEN_TECH = 'General technologies', _('General technologies')
