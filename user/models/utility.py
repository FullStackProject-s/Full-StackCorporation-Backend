from django.db import models


class TimeStampModelMixin(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Permissions(models.Model):
    """
    Model for custom staff role.
    Actual staff  it's [administrator, product_manager, developer]
    """
    STAFF_ROLE_SET = [
        ('admin', 'administrator'),
        ('prod manager', 'product manager'),
        ('dev', 'developer')
    ]
    role_name = models.CharField(
        choices=STAFF_ROLE_SET,
        max_length=200,
    )

    def __str__(self):
        return f'{self.role_name}'
