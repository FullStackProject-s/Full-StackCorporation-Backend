from django.db import models

from employee.models.generic import (
    BaseEmployeeGeneric,
    BaseProjectManagerDeveloperGeneric
)
from employee.models.consts import SkillLevel
from employee.models.technologies import Technologies


class Developer(BaseProjectManagerDeveloperGeneric):
    specialties = models.ManyToManyField(
        'employee.DeveloperOrganizationSpecialty',
        blank=True,
    )
    stack = models.ManyToManyField(
        Technologies,
        blank=True,
    )
    team = models.ForeignKey(
        'project.Team',
        on_delete=models.SET_NULL,
        related_name='developer_team',
        blank=True,
        null=True
    )
    skill_level = models.CharField(
        choices=SkillLevel.choices,
        max_length=200,
        default=SkillLevel.junior
    )

    def append_specialties(self, spec):
        self.specialties.add(spec)
        self.save()

    def __str__(self):
        return f'{self.profile.user} - {self.pk}'


class ProjectManager(BaseProjectManagerDeveloperGeneric):
    team = models.ForeignKey(
        'project.Team',
        on_delete=models.SET_NULL,
        related_name='project_manager_team',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.profile.user} - {self.pk}'


class Administrator(BaseEmployeeGeneric):
    def __str__(self):
        return f'{self.profile.user} - {self.pk}'
