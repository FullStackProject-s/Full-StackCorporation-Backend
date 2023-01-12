from employee.models import ProjectManager
from model_bakery import baker


def make_project_manager(
        number: int
) -> list[ProjectManager] | ProjectManager:
    project_managers = baker.make(
        'employee.ProjectManager',
        _quantity=number,
    )
    if number == 1:
        return project_managers[0]
    return project_managers
