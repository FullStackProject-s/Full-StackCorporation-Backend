from project.models import Project
from model_bakery import baker


def make_project(number: int) -> list[Project] | Project:
    projects = baker.make(
        'project.Project',
        _quantity=number,
    )
    if number == 1:
        return projects[0]
    return projects
