from typing import Type

from employee.models import (
    Developer,
    ProjectManager
)
from project.models import Team


def update_employee(
        team: Team,
        old_employee: Developer | ProjectManager,
        model_: Type[Developer | ProjectManager],
        new_employee: Developer | ProjectManager
) -> None:
    if old_employee:
        old_employee_ = model_.objects.get(pk=old_employee.pk)
        old_employee_.team = None
        old_employee_.save()
    new_employee.team = team

    new_employee.save()
