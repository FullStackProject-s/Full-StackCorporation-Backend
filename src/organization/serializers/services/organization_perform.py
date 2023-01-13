from project.models import Project


def _create_projects(instance):
    if projects := instance.projects.all():
        for project in projects:
            Project.objects.get(pk=project.pk).set_organization(instance)


def _update_projects(instance, validated_data):
    if projects := validated_data.get('projects', None):
        for project in instance.projects.all():
            project.organization = None
            project.save()

        for project in projects:
            project.organization = instance
            project.save()
