from user.tests.utils import create_users_list
from organization.models import Organization


def create_organizations(
        organizations_numbers: int,
        start=1
) -> list[Organization]:
    users = create_users_list(organizations_numbers, start=start)

    return [
        Organization.objects.create(
            organization_name=f'organization_{index}',
            owner=user,
        ) for index, user in enumerate(users, start=start)
    ]
