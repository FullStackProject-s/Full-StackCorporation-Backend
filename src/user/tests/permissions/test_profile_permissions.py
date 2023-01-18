from general.tests.generic import BaseTestCasePermissionsGeneric
from user.tests.test_profile import (
    BaseProfileTestCase,
)


class ProfilePermissionsTestCase(
    BaseProfileTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsOwnerOrReadOnlyProfile permission.
    """

    def test_get_all_profiles_perms(self):
        self._test_get_all_objects()

    def test_profile_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_profile_perms(self):
        self._test_delete_object_perms()

    def test_put_profile_perms(self):
        self._test_put_object_perms()

    def test_patch_profile_perms(self):
        self._test_put_object_perms()
