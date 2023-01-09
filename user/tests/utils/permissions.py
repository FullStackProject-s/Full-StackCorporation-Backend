from user.models.consts import StaffRole
from user.models import Permissions


def create_permissions() -> list[Permissions]:
    return [
        Permissions.objects.get_or_create(
            role_name=staff_role
        )[0] for staff_role in StaffRole.values
    ]
