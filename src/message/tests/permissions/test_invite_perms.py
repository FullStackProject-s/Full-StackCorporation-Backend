from rest_framework import status
from rest_framework.reverse import reverse

from general.tests.generic import BaseTestCasePermissionsGeneric
from general.tests.model_factory import (
    make_invite_to_organization,
    make_user,
    make_administrator
)
from message.tests.test_invite import (
    BaseInviteToOrganizationTestCase,
)


class InvitePermissionsTestCase(
    BaseInviteToOrganizationTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsAdministratorOrOwnerOrReadOnlyInvite permission.
    """

    def test_get_all_invites_perms(self):
        self._test_get_all_objects()

    def test_invite_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_invite_perms(self):
        self._test_delete_object_perms()

    def test_put_invite_perms(self):
        self._test_put_object_perms()

    def test_patch_invite_perms(self):
        self._test_patch_object_perms()

    def test_patch_invite_owner(self):
        invite = make_invite_to_organization(1)

        user = invite.creator
        user.is_active = True
        user.save()

        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': invite.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_invite_owner(self):
        invite = make_invite_to_organization(1)

        user = invite.creator
        user.is_active = True
        user.save()

        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': invite.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_patch_invite_owner_admin(self):
        invite = make_invite_to_organization(1)

        owner = make_user(1)
        admin = make_administrator(1)

        user = admin.profile.user
        user.is_active = True
        user.save()

        org = invite.to_organization

        org.owner = owner
        org.members.add(admin.profile.user)
        org.save()

        self._set_credentials_for_user(owner)
        self.client.force_login(owner)

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': invite.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': invite.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
