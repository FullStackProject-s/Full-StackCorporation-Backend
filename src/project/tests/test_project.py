from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from project.serializer import ProjectSerializer
from project.models import Project

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import (
    make_project,
    make_organization
)


class ProjectTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`project.Project`.
    """
    all_objects_url = reverse('all-projects')
    create_object_url = reverse('create-project')

    retrieve_object_url = 'project'
    delete_object_url = 'delete-project'
    update_object_url = 'update-project'

    make_method = make_project
    model_class = Project
    serializer_class = ProjectSerializer

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_projects(self):
        self._test_get_all_objects()

    def test_project_retrieve(self):
        proj = self.obj_1
        response_json = self._test_retrieve_object().json()
        self.assertEqual(
            response_json['project_name'],
            proj.project_name
        )

    def test_project_create(self):
        org = make_organization(1)

        json = {
            "project_name": "project_create",
            "organization": org.pk,
            "deadline": timezone.now().date() + timedelta(days=4)
        }
        self._test_create_object(json)

    def test_delete_project(self):
        self._test_delete_object()

    def test_put_project(self):
        org = make_organization(1)

        proj = self.obj_4
        self.default_object_number = 4

        delta = timedelta(days=4)
        json = {
            "project_name": "project_put",
            "organization": org.pk,
            "deadline": proj.deadline + delta
        }

        response_json = self._test_put_object(json).json()

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
        self.default_object_number = 4
        json = {
            "project_name": "project_patch"
        }

        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            response_json['project_name'],
            json['project_name']
        )
