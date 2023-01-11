from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from organization.models import Organization
from project.models import Project


@receiver(m2m_changed, sender=Organization.projects.through)
def set_organization_project(
        instance: Organization,
        action,
        pk_set,
        **kwargs
):
    match action:
        case 'post_add':
            for pk in pk_set:
                project = Project.objects.get(pk=pk)
                project.organization = instance
                project.save()
