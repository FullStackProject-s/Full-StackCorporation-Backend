from employee.models import DeveloperOrganizationSpecialty
from model_bakery import baker


def make_specialty(
        number: int
) -> list[DeveloperOrganizationSpecialty] | DeveloperOrganizationSpecialty:
    specialties = baker.make(
        'employee.DeveloperOrganizationSpecialty',
        _quantity=number,
    )
    if number == 1:
        return specialties[0]
    return specialties
