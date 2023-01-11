from user.tests.utils import create_users_list
from project.tests.utils import (
    create_projects,
    create_teams
)
from message.models import Reassignment


def create_reassignment(
        reassignment_numbers: int,
        start=1,
        keyword=''
) -> list[Reassignment]:
    keyword = 'create_reassignment' + keyword
    user = create_users_list(
        reassignment_numbers,
        start=reassignment_numbers,
        keyword=keyword
    )[0]

    proj_1, proj_2 = create_projects(
        reassignment_numbers + 1,
        start=reassignment_numbers,

    )
    team_1, team_2 = create_teams(
        reassignment_numbers + 1,
        start=reassignment_numbers,
        keyword=keyword
    )
    return [
        Reassignment.objects.create(
            creator=user,
            text=f'reassignment_{index}',
            from_project=proj_1,
            to_project=proj_2,
            from_team=team_1,
            to_team=team_2
        ) for index in range(
            start,
            reassignment_numbers + 1
        )
    ]
