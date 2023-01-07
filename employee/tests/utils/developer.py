from employee.models import Developer
from user.tests.utils import create_profiles
from employee.tests.utils import create_technologies
from random import randint
from employee.models.consts import (
    SkillLevel,
    Specialty
)


def create_developers(developer_number):
    skill_level_val = SkillLevel.values
    specialty_val = Specialty.values

    _min = min(len(specialty_val), len(skill_level_val)) - 1
    profiles_list = create_profiles(developer_number)
    return [
        Developer.objects.create(
            profile=profile,
            skill_level=skill_level_val[randint(0, _min)],
            specialty=specialty_val[randint(0, _min)],
        ) for profile in profiles_list
    ]
