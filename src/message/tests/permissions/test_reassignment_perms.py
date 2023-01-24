from rest_framework import status
from rest_framework.reverse import reverse

from general.tests.generic import BaseTestCasePermissionsGeneric
from general.tests.model_factory import (
    make_reassignment,
    make_organization,
    make_project,
    make_team,
    make_user,
    make_administrator
)
from message.tests.test_reassignment import (
    BaseReassignmentTestCase,
)


class ReassignmentPermissionsTestCase(
    BaseReassignmentTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsAdministratorOrOwnerOrReadOnlyInvite permission.
    """

    def test_get_all_reassignments_perms(self):
        self._test_get_all_objects()

    def test_reassignment_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_reassignment_perms(self):
        self._test_delete_object_perms()

    def test_put_reassignment_perms(self):
        self._test_put_object_perms()

    def test_patch_reassignment_perms(self):
        self._test_patch_object_perms()

    def test_create_reassignment_perms(self):
        org = make_organization(1)
        proj_1, proj_2 = make_project(2)
        team_1, team_2 = make_team(2)
        member = make_user(1)

        user = member
        user.is_active = True
        user.save()

        org.members.add(user)
        org.save()

        json = {
            "creator": user.pk,
            "text": "test_create_reassignment_perms",
            "organization": org.pk,
            "from_project": proj_1.pk,
            "to_project": proj_2.pk,
            "from_team": team_1.pk,
            "to_team": team_2.pk
        }
        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.post(
            self.create_object_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_reassignment_owner(self):
        reassignment = make_reassignment(1)

        user = reassignment.creator
        user.is_active = True
        user.save()

        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': reassignment.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_patch_reassignment_owner_admin(self):
        reassignment = make_reassignment(1)
        org = make_organization(1)

        reassignment.organization = org
        reassignment.save()

        owner = make_user(1)
        admin = make_administrator(1)

        user = admin.profile.user
        user.is_active = True
        user.save()

        org = reassignment.organization

        org.owner = owner
        org.members.add(admin.profile.user)
        org.save()

        self._set_credentials_for_user(owner)
        self.client.force_login(owner)

        url = reverse(self.update_object_url, kwargs={'pk': reassignment.pk})

        response = self.client.patch(
            url,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self._set_credentials_for_user(user)
        self.client.force_login(user)

        response = self.client.patch(
            url,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
