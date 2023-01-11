from user.tests.utils import create_users_list
from organization.models import Organization


def create_organizations(
        organizations_numbers: int,
        start=1,
        keyword=''
) -> list[Organization]:
    keyword = 'create_organizations' + keyword
    users = create_users_list(
        organizations_numbers,
        start=start,
        keyword=keyword
    )

    return [
        Organization.objects.create(
            organization_name=f'organization_{index}{keyword}',
            owner=user,
        ) for index, user in enumerate(users, start=start)
    ]
