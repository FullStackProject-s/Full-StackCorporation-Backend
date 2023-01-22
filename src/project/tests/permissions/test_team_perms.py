from django.urls import reverse
from rest_framework import status

from general.tests.generic import BaseTestCasePermissionsGeneric
from general.tests.model_factory import (
    make_team,
    make_project_manager,
    make_administrator
)

from project.tests.permissions.mixins import TestOwnerPermsMixin
from project.tests.test_team import BaseTeamTestCase


class TeamPermissionsTestCase(
    BaseTeamTestCase,
    BaseTestCasePermissionsGeneric,
    TestOwnerPermsMixin
):
    """
    Test Cases for IsProjectManagerOrAdministratorOrOwnerOrReadOnlyTeam
    permission.
    """

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_teams_perms(self):
        self._test_get_all_objects()

    def test_team_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_team_perms(self):
        self._test_delete_object_perms()

    def test_put_team_perms(self):
        self._test_put_object_perms()

    def test_patch_team_perms(self):
        self._test_patch_object_perms()

    def test_patch_team_manager_perms(self):
        team = make_team(1)

        proj_manager = make_project_manager(1)

        user = proj_manager.profile.user
        user.is_active = True
        user.save()

        team.project_manager = proj_manager
        team.save()

        self._run_patch_request_for_object(
            user,
            team
        )

    def test_patch_team_admin_perms(self):
        team = make_team(1)

        admin = make_administrator(1)

        user = admin.profile.user
        user.is_active = True
        user.save()

        team.project.organization.members.add(user)
        team.save()

        self.client.force_login(user)
        self._set_credentials_for_user(user)

        response = self.client.patch(
            reverse(
                self.update_object_url,
                kwargs={'pk': team.pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_patch_team_owner_perms(self):
        team = make_team(1)
        self._test_object_owner_perms(
            team,
            team.project.organization.pk
        )
