from django.db import models
from employee.models.consts import (
    TechnologiesStack,
    Specialty
)


class Technologies(models.Model):
    technology_name = models.CharField(max_length=200, unique=True)
    technology_category = models.CharField(
        choices=TechnologiesStack.choices,
        max_length=200
    )

    def __str__(self):
        return f'{self.technology_category} - {self.technology_name}'


class DeveloperOrganizationSpecialty(models.Model):
    specialty = models.CharField(
        choices=Specialty.choices,
        max_length=200,
    )
    organization_developer = models.ForeignKey(
        'employee.Developer',
        on_delete=models.CASCADE,
    )

    organization = models.ForeignKey(
        'organization.Organization',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.organization_developer} - ' \
               f'{self.organization} - ' \
               f'{self.specialty}'
