from employee.models import Developer
from project.models import Team


def update_developer(
        team: Team,
        developers: list[Developer]
):
    for old_dev in team.developers.all():
        developer = Developer.objects.get(pk=old_dev.pk)
        if team.team_lead != developer:
            developer.remove_team()
            old_dev.remove_team()

    for developer_ in developers:
        developer = Developer.objects.get(pk=developer_.pk)
        developer.set_team(team)
