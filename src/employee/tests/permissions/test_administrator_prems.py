from general.tests.generic import BaseTestCasePermissionsGeneric

from employee.tests.test_administrator import (
    BaseAdministratorTestCase,
)


class AdministratorPermissionsTestCase(
    BaseAdministratorTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsOwnerOrReadOnlyEmployee permission.
    """

    def test_get_all_administrators_perms(self):
        self._test_get_all_objects()

    def test_administrator_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_administrator_perms(self):
        self._test_delete_object_perms()

    def test_put_administrator_perms(self):
        self._test_put_object_perms()

    def test_patch_administrator_perms(self):
        self._test_patch_object_perms()
