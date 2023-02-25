from project.models import Project


def add_organization_in_project(instance: Project, validated_data) -> Project:
    organization = validated_data.get('organization')
    organization.projects.add(instance)
    organization.save()
    return instance
