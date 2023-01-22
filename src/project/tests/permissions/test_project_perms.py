from django.urls import reverse
from rest_framework import status

from general.tests.generic import BaseTestCasePermissionsGeneric
from general.tests.model_factory import (
    make_organization,
    make_user,
    make_project,
    make_administrator
)

from project.tests.permissions.mixins import TestOwnerPermsMixin
from project.tests.test_project import BaseProjectTestCase


class ProjectPermissionsTestCase(
    BaseProjectTestCase,
    BaseTestCasePermissionsGeneric,
    TestOwnerPermsMixin
):
    """
    Test Cases for IsOwnerOrReadOnlyEmployee permission.
    """

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        for index, (org, owner) in enumerate(zip(
                make_organization(cls.number_of_objects),
                make_user(cls.number_of_objects)),
                start=1
        ):
            project = getattr(cls, f'obj_{index}')
            org.projects.add(project)
            project.set_organization(org)
            org.owner = owner

            org.save()

    def test_get_all_projects_perms(self):
        self._test_get_all_objects()

    def test_project_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_project_perms(self):
        self._test_delete_object_perms()

    def test_put_project_perms(self):
        self._test_put_object_perms()

    def test_patch_project_perms(self):
        self._test_patch_object_perms()

    def test_patch_project_admin_perms(self):
        project = make_project(1)

        admin = make_administrator(1)

        user = admin.profile.user
        user.is_active = True
        user.save()

        project.organization.members.add(user)
        project.save()

        self.client.force_login(user)
        self._set_credentials_for_user(user)

        response = self.client.patch(
            reverse(
                self.update_object_url,
                kwargs={'pk': project.pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_patch_project_owner_perms(self):
        project = make_project(1)
        self._test_object_owner_perms(
            project,
            project.organization.pk
        )
