from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        if not kwargs.get('is_active'):
            raise ValueError('User must be active')
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if not kwargs.get('is_active'):
            raise ValueError('Superuser must be active')
        if not kwargs.get('is_staff'):
            raise ValueError('Superuser must be staff')
        if not kwargs.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **kwargs)


class Permissions(models.Model):
    role_name = models.CharField(max_length=200, unique=True)


class CustomUser(
    AbstractBaseUser,
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

    custom_permission = models.ForeignKey(
        Permissions,
        on_delete=models.CASCADE,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name'
    ]

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
