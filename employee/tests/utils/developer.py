from employee.models import Developer
from employee.models.consts import (
    SkillLevel,
    Specialty
)
from user.tests.utils import create_profiles

from random import randint


def create_developers(developer_number: int, start=1) -> list[Developer]:
    skill_level_val = SkillLevel.values

    _min = len(skill_level_val) - 1
    pks = [
        Developer.objects.create(
            profile=profile,
            skill_level=skill_level_val[randint(0, _min)]
        ).pk for profile in create_profiles(developer_number, start=start)
    ]
    return [
        Developer.objects.get(
            pk=pk
        ) for pk in pks
    ]
