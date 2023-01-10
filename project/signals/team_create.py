from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from project.models import Team
from project.serializer import TeamShowSerializer

from employee.models import (
    Developer,
    ProjectManager
)


@receiver(post_save, sender=Team)
def set_employee_team(
        sender,
        instance: Team,
        created,
        **kwargs
):
    if created:
        if team_lead_ := instance.team_lead:
            team_lead = Developer.objects.get(pk=team_lead_.pk)
            team_lead.team = instance
            team_lead.save()
        if project_manger_ := instance.project_manager:
            project_manger = ProjectManager.objects.get(pk=project_manger_.pk)
            project_manger.team = instance
            project_manger.save()


@receiver(m2m_changed, sender=Team.developers.through)
def set_developers_team(
        instance: Team,
        action,
        pk_set,
        **kwargs
):
    match action:
        case 'post_add':
            for pk in pk_set:
                developer_ = Developer.objects.get(pk=pk)
                developer_.team = instance
                developer_.save()
