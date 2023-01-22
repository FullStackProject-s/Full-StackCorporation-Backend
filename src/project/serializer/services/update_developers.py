from employee.models import Developer
from project.models import Team


def update_developer(
        team: Team,
        developers: list[Developer]
):
    for old_dev in team.developers.all():
        if team.team_lead != old_dev:
            old_dev.remove_team()

    for developer_ in developers:
        developer = Developer.objects.get(pk=developer_.pk)
        developer.set_team(team)
