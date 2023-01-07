from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from user.models.utility import TimeStampModelMixin, Permissions
from user.managers import UserManager


class CustomUser(
    AbstractBaseUser,
    TimeStampModelMixin,
    PermissionsMixin
):
    username = models.CharField(
        max_length=125,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    staff_role = models.ForeignKey(
        Permissions,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
        'password',
    ]

    def __str__(self):
        return f"{self.username} - {self.pk}"
