from user.models.consts import StaffRole
from user.models import Permissions


def create_permissions(permission: StaffRole.values) -> Permissions:
    return Permissions.objects.get_or_create(role_name=permission)[0]
