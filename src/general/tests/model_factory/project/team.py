from project.models import Team
from model_bakery import baker


def make_team(number: int) -> list[Team] | Team:
    teams = baker.make(
        'project.Team',
        _quantity=number,
    )
    if number == 1:
        return teams[0]
    return teams
