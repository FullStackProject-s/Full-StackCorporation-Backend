from rest_framework import serializers

from organization.models import Organization
from project.models import Project


class UniqueProjectForOrganizationMixin:
    def _validate_projects_field(
            self,
            projects: list[Project]
    ) -> list[Project]:
        for project in projects:
            org = Organization.objects.filter(
                projects=project
            )
            if org.exists() and self.instance not in org:
                raise serializers.ValidationError(
                    "Project already used in different organization"
                )
        return projects
