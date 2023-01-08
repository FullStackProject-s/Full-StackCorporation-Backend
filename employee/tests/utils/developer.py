from employee.models import Developer
from employee.models.consts import (
    SkillLevel,
    Specialty
)
from user.tests.utils import create_profiles

from random import randint


def create_developers(developer_number, start=1):
    skill_level_val = SkillLevel.values
    specialty_val = Specialty.values

    _min = min(len(specialty_val), len(skill_level_val)) - 1
    profiles_list = create_profiles(developer_number, start=start)
    return [
        Developer.objects.create(
            profile=profile,
            skill_level=skill_level_val[randint(0, _min)],
            # specialty=specialty_val[randint(0, _min)],
        ) for profile in profiles_list
    ]
