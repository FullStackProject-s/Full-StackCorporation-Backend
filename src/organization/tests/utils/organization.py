from general.tests.model_factory import make_user
from organization.models import Organization


def create_organizations(
        organizations_numbers: int,
        start=1,
        keyword=''
) -> list[Organization]:
    keyword = 'create_organizations' + keyword
    users = make_user(
        organizations_numbers,
    )

    return [
        Organization.objects.create(
            organization_name=f'organization_{index}{keyword}',
            owner=user,
        ) for index, user in enumerate(users, start=start)
    ]
