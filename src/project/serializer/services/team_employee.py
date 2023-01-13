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
        model_.objects.get(pk=old_employee.pk).set_team(None)
    new_employee.set_team(team)
