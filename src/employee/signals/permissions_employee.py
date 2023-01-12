from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from employee.models import (
    Administrator,
    ProjectManager,
    Developer
)
from general.signals import suspending_receiver

from user.models.consts import StaffRole
from user.models import Permissions

User = get_user_model()


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
        instance.profile.user.staff_role = perms
        instance.save()


@suspending_receiver(post_save, sender=ProjectManager)
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
        instance.profile.user.staff_role = perms
        instance.save()


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

        user = User.objects.get(pk=instance.profile.user.pk)
        instance.profile.user.staff_role = perms
        user.staff_role = perms
        instance.save()
        user.save()
