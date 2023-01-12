from employee.models import ProjectManager
from general.tests.model_factory import make_profile


def create_project_managers(project_manager_number, start=1):
    profiles_list = make_profile(project_manager_number)
    pks = []
    for profile in profiles_list:
        pks.append(
            ProjectManager.objects.create(
                profile=profile
            ).pk)
    return [
        ProjectManager.objects.get(
            pk=pk
        ) for pk in pks
    ]
