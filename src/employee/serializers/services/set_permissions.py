from django.contrib.auth import get_user_model

from user.models import Permissions
from user.models.consts import StaffRole

User = get_user_model()


def set_perms_for_employee(role_name: StaffRole, instance):
    perms, created = Permissions.objects.get_or_create(
        role_name=role_name
    )

    user = User.objects.get(pk=instance.profile.user.pk)
    instance.profile.user.staff_role = perms
    user.staff_role = perms

    instance.save()
    user.save()
