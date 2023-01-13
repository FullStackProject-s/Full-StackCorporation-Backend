from django.db.models.signals import post_save
from django.dispatch import receiver

from employee.models import (
    Administrator,
    ProjectManager,
    Developer
)
from employee.signals.services import set_perms_for_employee

from user.models.consts import StaffRole
from user.models import Permissions


@receiver(post_save, sender=Administrator)
def set_admin_permission(
        sender,
        instance: Administrator,
        created,
        **kwargs
):
    if created:
        perms, created = Permissions.objects.get_or_create(
            role_name=StaffRole.ADMIN
        )
        set_perms_for_employee(instance, perms)


@receiver(post_save, sender=ProjectManager)
def set_project_manager_permission(
        sender,
        instance: ProjectManager,
        created,
        **kwargs
):
    if created:
        perms, created = Permissions.objects.get_or_create(
            role_name=StaffRole.PRODUCT_MANAGER
        )
        set_perms_for_employee(instance, perms)


@receiver(post_save, sender=Developer)
def set_developer_permission(
        sender,
        instance: Developer,
        created,
        **kwargs
):
    if created:
        perms, created = Permissions.objects.get_or_create(
            role_name=StaffRole.DEVELOPER
        )
        set_perms_for_employee(instance, perms)
