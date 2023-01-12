from employee.models import Administrator
from general.tests.model_factory import make_profile


def create_administrators(admin_numbers):
    profiles_list = make_profile(admin_numbers)
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
