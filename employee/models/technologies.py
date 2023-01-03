from django.db import models
from employee.models.consts import SPECIALTY_SET


class Technologies(models.Model):
    TECHNOLOGIES_STACK = [
        *SPECIALTY_SET,
        ('Gen tech', 'General technologies')
    ]
    technology_name = models.CharField(max_length=200, unique=True)
    technology_category = models.CharField(
        choices=TECHNOLOGIES_STACK,
        max_length=200
    )

    def __str__(self):
        return f'{self.technology_category} - {self.technology_name}'
