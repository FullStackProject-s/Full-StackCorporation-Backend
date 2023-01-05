from django.db import models

from employee.models.mixins.baseEmployee import BaseEmployeeMixin
from employee.models.consts import Specialty
from employee.models.technologies import Technologies


class Developer(BaseEmployeeMixin):
    specialty = models.CharField(
        choices=Specialty.choices,
        max_length=200
    )
    stack = models.ManyToManyField(
        Technologies,
        blank=True,
    )
    team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE,
        related_name='developer_team',
        blank=True,
        null=True
    )

    def append_technologies(self, tech_list):
        self.stack.add(*tech_list)
        self.save()

    def remove_technologies(self, tech):
        self.stack.remove(tech)
        self.save()

    def __str__(self):
        return f'{self.specialty} - {self.profile.user} - {self.pk}'


class ProjectManager(BaseEmployeeMixin):
    team = models.ForeignKey(
        'project.Team',
        on_delete=models.CASCADE,
        related_name='project_manager_team',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.profile.user} - {self.pk}'


class Administrator(BaseEmployeeMixin):
    def __str__(self):
        return f'{self.profile.user} - {self.pk}'
