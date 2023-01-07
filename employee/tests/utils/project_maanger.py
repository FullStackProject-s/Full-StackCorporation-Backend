from employee.models import ProjectManager
from user.tests.utils import create_profiles


def create_project_managers(project_manager):
    profiles_list = create_profiles(project_manager)
    return [
        ProjectManager.objects.create(
            profile=profile
        ) for profile in profiles_list
    ]
