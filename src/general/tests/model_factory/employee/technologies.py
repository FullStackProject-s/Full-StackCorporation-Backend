from employee.models import Technologies
from model_bakery import baker


def make_technologies(
        number: int
) -> list[Technologies] | Technologies:
    technologies = baker.make(
        'employee.Technologies',
        _quantity=number,
    )
    if number == 1:
        return technologies[0]
    return technologies
