from django.urls import reverse
from rest_framework import status

from general.tests.generic import BaseTestCaseGeneric

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from general.tests.model_factory import (
    make_organization,
    make_project,
    make_user
)

from project.models import Project


class BaseOrganizationTestCase(BaseTestCaseGeneric):
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


class OrganizationTestCase(BaseOrganizationTestCase):
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
        json = {
            "organization_name": "create_org",
        }
        response_json = self._test_create_object(json).json()
        self.assertEqual(
            response_json['owner']['pk'],
            self.base_login_user.pk
        )

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

        org.projects.add(proj_1)
        proj_1.set_organization(org)

        org.projects.add(proj_2)
        proj_2.set_organization(org)

        org.projects.add(proj_3)
        proj_3.set_organization(org)

        org.projects.add(proj_4)
        proj_4.set_organization(org)

        org.save()

        self.assertListEqual(
            list(Organization.objects.get(pk=pk).projects.all()),
            [proj_1, proj_2, proj_3, proj_4]
        )
        self.assertEqual(
            Project.objects.get(pk=proj_1.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_2.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_3.pk).organization,
            org
        )
        self.assertEqual(
            Project.objects.get(pk=proj_4.pk).organization,
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
            Project.objects.filter(pk=proj_1.pk).exists(),
            False
        )
        self.assertEqual(
            Project.objects.filter(pk=proj_2.pk).exists(),
            False
        )

    def test_project_for_one_organization(self):
        org_1, org_2 = make_organization(2)
        proj = make_project(1)
        json = {
            'projects': [
                proj.pk
            ]
        }
        response = self.client.patch(
            reverse(
                self.update_object_url,
                kwargs={'pk': org_1.pk}
            ),
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        response = self.client.patch(
            reverse(
                self.update_object_url,
                kwargs={'pk': org_2.pk}
            ),
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
