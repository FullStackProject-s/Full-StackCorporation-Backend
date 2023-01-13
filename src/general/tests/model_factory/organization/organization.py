from organization.models import Organization
from model_bakery import baker


def make_organization(number: int) -> list[Organization] | Organization:
    organizations = baker.make(
        'organization.Organization',
        _quantity=number,
    )
    if number == 1:
        return organizations[0]
    return organizations
