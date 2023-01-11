from employee.models import Administrator
from user.tests.utils import create_profiles


def create_administrators(admin_numbers):
    profiles_list = create_profiles(admin_numbers)
    pks = []
    for profile in profiles_list:
        pks.append(
            Administrator.objects.create(
                profile=profile
            ).pk)
    return [
        Administrator.objects.get(
            pk=pk
        ) for pk in pks
    ]
