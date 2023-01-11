from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from organization.models import Organization
from organization.serializers import OrganizationSerializer
from organization.tests.utils import create_organizations

from project.models import Project
from project.tests.utils import create_projects

from user.tests.utils import create_users_list


class OrganizationTestCase(APITestCase):
    """
    Test Cases for :model:`organization.Organization`.
    """
    all_organization_url = reverse('all-organizations')
    create_organization_url = reverse('organization-create')

    retrieve_organization = 'organization'
    delete_organization = 'delete-organization'
    update_organization = 'update-organization'

    number_of_organizations = 4

    @classmethod
    def setUpTestData(cls):
        for index, profile in enumerate(
                create_organizations(cls.number_of_organizations),
                start=1
        ):
            setattr(
                cls,
                f'org_{index}',
                profile
            )

    def setUp(self) -> None:
        self.client.force_login(self.org_1.owner)

    def test_get_all_organizations(self):
        response = self.client.get(self.all_organization_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.number_of_organizations
        )

    def test_organization_retrieve(self):
        org = self.org_1
        pk = org.pk
        response = self.client.get(
            reverse(self.retrieve_organization, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['organization_name'],
            org.organization_name
        )
        self.assertEqual(
            response_json,
            OrganizationSerializer(org).data
        )

    def test_organization_create(self):
        start = abs(hash('test_organization_create'))
        user = create_users_list(start, start=start)[0]

        json = {
            "organization_name": "create_org",
            "user": user.pk
        }
        response = self.client.post(
            self.create_organization_url,
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
            OrganizationSerializer(Organization.objects.get(pk=pk)).data
        )

    def test_delete_organization(self):
        pk = self.org_1.pk

        response = self.client.delete(
            reverse(
                self.delete_organization,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Organization.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_organization(self):
        name = 'test_put_organization'
        start = abs(hash(name))
        user = create_users_list(start, start=start)[0]

        org = self.org_2
        pk = org.pk
        json = {
            "organization_name": name,
            "user": user.pk
        }
        response = self.client.put(
            reverse(
                self.update_organization,
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
            response_json['organization_name'],
            json['organization_name'],
        )

    def test_patch_organization(self):
        org = self.org_2
        pk = org.pk
        json = {
            "organization_name": "test_patch_organization",
        }
        response = self.client.patch(
            reverse(
                self.update_organization,
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
            response_json['organization_name'],
            json['organization_name'],
        )
        self.assertNotEqual(
            response_json['organization_name'],
            org.organization_name,
        )

    def test_project_organization_signal(self):
        org = self.org_2
        name = 'test_project_organization_signal'
        start = abs(hash(name))

        proj_1, proj_2, proj_3, proj_4 = create_projects(
            start + 3,
            start=start
        )

        json = {
            "projects": [
                proj_1.pk,
                proj_2.pk
            ],
        }
        response = self.client.patch(
            reverse(
                self.update_organization,
                kwargs={'pk': org.pk}
            ),
            data=json,
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
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
        response = self.client.patch(
            reverse(
                self.update_organization,
                kwargs={'pk': org.pk}
            ),
            data=json,
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
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
