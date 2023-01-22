from django.urls import reverse
from rest_framework import status

from general.tests.generic import BaseTestCasePermissionsGeneric
from organization.tests.test_organization import (
    BaseOrganizationTestCase,
)
from general.tests.model_factory import (
    make_organization,
    make_user,
    make_administrator
)


class OrganizationPermissionsTestCase(
    BaseOrganizationTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsAdministratorOrOwnerOrReadOnlyOrganization permission.
    """

    def test_get_all_organizations_perms(self):
        self._test_get_all_objects()

    def test_organization_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_organization_perms(self):
        self._test_delete_object_perms()

    def test_delete_organization_owner_perms(self):
        organization, owner = self.__get_organization_owner()

        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': organization.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_delete_organization_admin_perms(self):
        organization, user_admin = self.__get_organization_admin()

        self.client.force_login(user_admin)
        self._set_credentials_for_user(user_admin)

        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': organization.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_put_organization_perms(self):
        self._test_put_object_perms()

    def test_put_organization_owner_perms(self):
        organization, owner = self.__get_organization_owner()

        json = {
            'organization_name': 'test_put_organization_owner_perms'
        }
        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        response = self.client.put(
            reverse(self.update_object_url, kwargs={'pk': organization.pk}),
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_put_organization_admin_perms(self):
        organization, user_admin = self.__get_organization_admin()

        json = {
            'organization_name': 'test_put_organization_admin_perms'
        }

        self.client.force_login(user_admin)
        self._set_credentials_for_user(user_admin)

        response = self.client.put(
            reverse(self.update_object_url, kwargs={'pk': organization.pk}),
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_patch_organization_owner_perms(self):
        organization, owner = self.__get_organization_owner()

        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': organization.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_patch_organization_admin_perms(self):
        organization, user_admin = self.__get_organization_admin()

        self.client.force_login(user_admin)
        self._set_credentials_for_user(user_admin)

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': organization.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_patch_organization_perms(self):
        self._test_patch_object_perms()

    def __get_organization_owner(self):
        organization = make_organization(1)
        owner = make_user(1)
        organization.owner = owner
        organization.save()
        return organization, owner

    def __get_organization_admin(self):
        organization = make_organization(1)

        user_admin = make_administrator(1).profile.user
        user_admin.is_active = True
        user_admin.save()

        organization.members.add(user_admin)
        organization.save()
        return organization, user_admin
