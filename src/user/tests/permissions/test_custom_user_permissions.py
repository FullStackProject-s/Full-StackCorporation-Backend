from general.tests.generic import BaseTestCasePermissionsGeneric
from user.tests.test_user import (
    BaseCustomUserTestCase,
)


class CustomUserPermissionsTestCase(
    BaseCustomUserTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsOwnerOrReadOnlyCustomUser permission.
    """

    def test_get_all_users_perms(self):
        self._test_get_all_objects()

    def test_user_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_user_perms(self):
        self._test_delete_object_perms()

    def test_put_user_perms(self):
        self._test_put_object_perms()

    def test_patch_user_perms(self):
        self._test_patch_object_perms()
