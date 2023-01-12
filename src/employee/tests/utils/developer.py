from employee.models import Developer
from employee.models.consts import SkillLevel

from general.tests.model_factory import make_profile

from random import randint


def create_developers(developer_number: int, start=1) -> list[Developer]:
    skill_level_val = SkillLevel.values

    _min = len(skill_level_val) - 1
    pks = [
        Developer.objects.create(
            profile=profile,
            skill_level=skill_level_val[randint(0, _min)]
        ).pk for profile in make_profile(developer_number)
    ]
    return [
        Developer.objects.get(
            pk=pk
        ) for pk in pks
    ]
