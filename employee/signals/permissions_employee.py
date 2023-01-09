from django.db.models.signals import post_save
from django.dispatch import receiver

from employee.models import Administrator

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
        instance.profile.user.staff_role = perms
        instance.save()
