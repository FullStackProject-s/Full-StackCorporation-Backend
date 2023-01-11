from project.models import Team


def create_teams(
        team_number,
        start=1,
        keyword=''
):
    keyword = 'create_teams' + keyword
    return [
        Team.objects.create(
            team_name=f'team_{index}{keyword}'
        ) for index in range(start, team_number + 1)
    ]
