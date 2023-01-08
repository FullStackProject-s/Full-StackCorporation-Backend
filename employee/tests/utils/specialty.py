from employee.models import DeveloperOrganizationSpecialty
from employee.models.consts import Specialty
from employee.tests.utils import create_developers

from organization.tests.utils import create_organizations
from random import randint


def create_specialities(spec_numbers: int, start=1):
    orgs_start = abs(hash('create_organizations'))
    devs_start = abs(hash('create_developers'))
    orgs = create_organizations(orgs_start + spec_numbers - 1, start=orgs_start)
    devs = create_developers(devs_start + spec_numbers - 1, start=devs_start)
    return [
        DeveloperOrganizationSpecialty.objects.create(
            organization=org,
            organization_developer=dev,
            specialty=Specialty.values[randint(0, len(Specialty.values) - 1)]
        ) for index, (org, dev) in enumerate(
            zip(orgs, devs),
            start=start
        )
    ]
