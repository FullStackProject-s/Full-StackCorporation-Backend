from project.models import Project


def create_projects(instance):
    if projects := instance.projects.all():
        for project in projects:
            Project.objects.get(pk=project.pk).set_organization(instance)


def update_projects(instance, validated_data):
    if projects := validated_data.get('projects', None):
        for project in instance.projects.all():
            project.remove_organization()

        for project in projects:
            project.set_organization(instance)
