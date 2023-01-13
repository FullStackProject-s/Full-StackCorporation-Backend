from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from general.tests.model_factory import (
    make_organization,
    make_project,
    make_user
)

from project.models import Project


class OrganizationTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`organization.Organization`.
    """
    all_objects_url = reverse('all-organizations')
    create_object_url = reverse('organization-create')

    retrieve_object_url = 'organization'
    delete_object_url = 'delete-organization'
    update_object_url = 'update-organization'

    make_method = make_organization
    model_class = Organization
    serializer_class = OrganizationSerializer

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_organizations(self):
        self._test_get_all_objects()

    def test_organization_retrieve(self):
        org = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['organization_name'],
            org.organization_name
        )

    def test_organization_create(self):
        user = make_user(1)

        json = {
            "organization_name": "create_org",
            "user": user.pk
        }
        self._test_create_object(json)

    def test_delete_organization(self):
        self._test_delete_object()

    def test_put_organization(self):
        user = make_user(1)
        self.default_object_number = 2
        json = {
            "organization_name": 'test_put_organization',
            "user": user.pk
        }
        response_json = self._test_put_object(json).json()
        self.assertEqual(
            response_json['organization_name'],
            json['organization_name'],
        )

    def test_patch_organization(self):
        org = self.obj_2
        self.default_object_number = 2
        json = {
            "organization_name": "test_patch_organization",
        }
        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            response_json['organization_name'],
            json['organization_name'],
        )
        self.assertNotEqual(
            response_json['organization_name'],
            org.organization_name,
        )

    def test_project_organization_sets(self):
        org = self.obj_3
        self.default_object_number = 3
        pk = org.pk
        proj_1, proj_2, proj_3, proj_4 = make_project(4)

        json = {
            "projects": [
                proj_1.pk,
                proj_2.pk
            ],
        }
        self._test_patch_object(json).json()

        self.assertListEqual(
            list(Organization.objects.get(pk=pk).projects.all()),
            [proj_1, proj_2]
        )
        self.assertEqual(
            Project.objects.get(pk=proj_1.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_2.pk).organization,
            org
        )

        json = {
            "projects": [
                proj_3.pk,
                proj_4.pk
            ],
        }
        self._test_patch_object(json).json()

        self.assertEqual(
            list(Organization.objects.get(pk=pk).projects.all()),
            [proj_3, proj_4]
        )
        self.assertEqual(
            Project.objects.get(pk=proj_3.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_4.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_1.pk).organization,
            None
        )
        self.assertEqual(
            Project.objects.get(pk=proj_2.pk).organization,
            None
        )
