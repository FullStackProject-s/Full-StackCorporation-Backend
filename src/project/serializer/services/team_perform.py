from employee.models import Developer, ProjectManager
from project.serializer.services import (
    update_employee,
    update_developer
)


def update_personal(team, validated_data):
    if team_lead := validated_data.get('team_lead', None):
        update_employee(
            team,
            team.team_lead,
            Developer,
            team_lead
        )

    if project_manager := validated_data.get('project_manager', None):
        update_employee(
            team,
            team.project_manager,
            ProjectManager,
            project_manager
        )

    if developers := validated_data.get('developers', None):
        update_developer(team, developers)

    return team


def create_personal(instance):
    if team_lead_ := instance.team_lead:
        Developer.objects.get(pk=team_lead_.pk).set_team(instance)
    if project_manger_ := instance.project_manager:
        ProjectManager.objects.get(pk=project_manger_.pk).set_team(instance)
    if developers := instance.developers.all():
        for developer in developers:
            developer.set_team(instance)
