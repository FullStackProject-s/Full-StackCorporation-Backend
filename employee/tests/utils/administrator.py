from employee.models import Administrator
from user.tests.utils import create_profiles


def create_administrators(admin_numbers):
    profiles_list = create_profiles(admin_numbers)
    return [
        Administrator.objects.create(
            profile=profile
        ) for profile in profiles_list
    ]
