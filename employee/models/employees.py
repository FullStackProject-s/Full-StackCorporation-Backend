from django.db import models
from employee.models.mixins.baseEmployee import BaseEmployeeMixin
from employee.models.consts import SPECIALTY_SET
from employee.models.technologies import Technologies


class Developer(BaseEmployeeMixin):
    specialty = models.CharField(
        choices=SPECIALTY_SET,
        max_length=200
    )
    stack = models.ManyToManyField(Technologies)

    def __str__(self):
        return f'{self.specialty} - {self.profile.user}'


class ProjectManager(BaseEmployeeMixin):
    pass


class Administrator(models.Model):
    profile = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE
    )
