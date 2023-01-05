from django.utils.translation import gettext_lazy as _
from django.db import models


class StaffRole(models.TextChoices):
    ADMIN = 'Admin', _('Administrator')
    PRODUCT_MANAGER = 'Prod manager', _('Product manager')
    DEVELOPER = 'Dev', _('Developer')

