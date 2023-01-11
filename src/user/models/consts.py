from django.utils.translation import gettext_lazy as _
from django.db import models


class StaffRole(models.TextChoices):
    ADMIN = 'Administrator', _('Administrator')
    PRODUCT_MANAGER = 'Product manager', _('Product manager')
    DEVELOPER = 'Developer', _('Developer')
