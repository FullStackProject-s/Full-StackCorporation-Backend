from project.models import Project
from datetime import timedelta
from django.utils import timezone
from organization.tests.utils import create_organizations
from random import randint


def create_projects(project_number, start=1):
    organizations = create_organizations(project_number, start=start)
    return [
        Project.objects.create(
            project_name=f'project_{index}',
            organization=organization,
            deadline=timezone.now().date() + timedelta(days=randint(1, 20))
        ) for index, organization in enumerate(
            organizations,
            start=start
        )
    ]
