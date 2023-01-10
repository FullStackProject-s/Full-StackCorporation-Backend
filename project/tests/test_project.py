from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status

from organization.tests.utils import create_organizations

from project.serializer import ProjectSerializer
from project.models import Project
from project.tests.utils import create_projects


class ProjectTestCase(APITestCase):
    """
    Test Cases for :model:`project.Project`.
    """
    all_projects_url = reverse('all-projects')
    create_project_url = reverse('create-project')

    retrieve_project = 'project'
    delete_project = 'delete-project'
    update_project = 'update-project'

    number_of_projects = 4

    @classmethod
    def setUpTestData(cls):
        for index, project in enumerate(
                create_projects(cls.number_of_projects),
                start=1
        ):
            setattr(cls,
                    f'proj_{index}',
                    project
                    )

    def setUp(self) -> None:
        self.client.force_login(self.proj_1.organization.owner)

    def test_get_all_projects(self):
        response = self.client.get(self.all_projects_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.number_of_projects
        )

    def test_project_retrieve(self):
        proj = self.proj_1
        pk = proj.pk
        response = self.client.get(
            reverse(self.retrieve_project, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['project_name'],
            proj.project_name
        )
        self.assertEqual(
            response_json,
            ProjectSerializer(proj).data
        )

    def test_project_create(self):
        start = abs(hash('test_project_create'))
        org = create_organizations(start, start=start)[0]

        json = {
            "project_name": "project_create",
            "organization": org.pk,
            "deadline": timezone.now().date() + timedelta(days=4)
        }
        response = self.client.post(
            self.create_project_url,
            data=json,
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            ProjectSerializer(Project.objects.get(pk=pk)).data
        )

    def test_delete_project(self):
        pk = self.proj_1.pk

        response = self.client.delete(
            reverse(
                self.delete_project,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Project.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_project(self):
        name = 'test_put_project'
        start = abs(hash(name))
        org = create_organizations(start, start=start)[0]

        proj = self.proj_4
        pk = proj.pk
        delta = timedelta(days=4)
        json = {
            "project_name": "project_put",
            "organization": org.pk,
            "deadline": proj.deadline + delta
        }
        response = self.client.put(
            reverse(
                self.update_project,
                kwargs={'pk': pk}
            ),
            data=json,
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Project.objects.get(pk=proj.pk).deadline,
            proj.deadline + delta
        )
        self.assertEqual(
            response_json['project_name'],
            json['project_name']
        )
        self.assertEqual(
            response_json['deadline'],
            str(json['deadline']),
        )

    def test_patch_project(self):
        proj = self.proj_4
        pk = proj.pk
        json = {
            "project_name": "project_patch"
        }
        response = self.client.patch(
            reverse(
                self.update_project,
                kwargs={'pk': pk}
            ),
            data=json,
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['project_name'],
            json['project_name']
        )