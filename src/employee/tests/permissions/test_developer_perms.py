from general.tests.generic import BaseTestCasePermissionsGeneric

from employee.tests.test_developer import (
    BaseDeveloperTestCase,
)


class DeveloperPermissionsTestCase(
    BaseDeveloperTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsOwnerOrReadOnlyEmployee permission.
    """

    def test_get_all_developers_perms(self):
        self._test_get_all_objects()

    def test_developer_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_developer_perms(self):
        self._test_delete_object_perms()

    def test_put_developer_perms(self):
        self._test_put_object_perms()

    def test_patch_developer_perms(self):
        self._test_put_object_perms()
