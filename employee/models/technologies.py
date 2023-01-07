from django.db import models
from employee.models.consts import TechnologiesStack


class Technologies(models.Model):
    technology_name = models.CharField(max_length=200, unique=True)
    technology_category = models.CharField(
        choices=TechnologiesStack.choices,
        max_length=200
    )

    def __str__(self):
        return f'{self.technology_category} - {self.technology_name}'
