from employee.models import Developer
from model_bakery import baker


def make_developer(
        number: int
) -> list[Developer] | Developer:
    developers = baker.make(
        'employee.Developer',
        _quantity=number,
    )
    if number == 1:
        return developers[0]
    return developers
