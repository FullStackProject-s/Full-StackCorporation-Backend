from django.db import models

from user.models.consts import StaffRole


class Permissions(models.Model):
    """
    Model for custom staff role.
    Actual staff  it's [administrator, product_manager, developer]
    """

    role_name = models.CharField(
        choices=StaffRole.choices,
        max_length=200,
        unique=True
    )

    def __str__(self):
        return f'{self.role_name} - {self.pk}'
