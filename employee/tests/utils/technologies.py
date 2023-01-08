from employee.models import Technologies
from employee.models.consts import TechnologiesStack


def create_technologies(start=1):
    return [
        Technologies.objects.create(
            technology_name=f'tech_{index}',
            technology_category=value
        ) for index, value in enumerate(
            TechnologiesStack.values,
            start=start
        )
    ]
