from model_bakery import baker

from user.models import Permissions
from user.models.consts import StaffRole


def create_permissions() -> list[Permissions]:
    return [
        Permissions.objects.get_or_create(
            role_name=staff_role
        )[0] for staff_role in StaffRole.values
    ]


def make_permission(number: int) -> list[Permissions] | Permissions:
    permissions = create_permissions()
    if number == 1:
        return permissions[0]
    return permissions
