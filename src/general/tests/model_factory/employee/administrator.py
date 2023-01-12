from employee.models import Administrator
from model_bakery import baker


def make_administrator(
        number: int
) -> list[Administrator] | Administrator:
    administrators = baker.make(
        'employee.Administrator',
        _quantity=number,
    )
    if number == 1:
        return administrators[0]
    return administrators
