from general.tests.generic import BaseTestCasePermissionsGeneric

from employee.tests.test_project_manager import (
    BaseProjectManagerTestCase,
)


class ProjectManagerPermissionsTestCase(
    BaseProjectManagerTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsOwnerOrReadOnlyEmployee permission.
    """

    def test_get_all_project_managers_perms(self):
        self._test_get_all_objects()

    def test_project_manager_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_project_manager_perms(self):
        self._test_delete_object_perms()

    def test_put_project_manager_perms(self):
        self._test_put_object_perms()

    def test_patch_project_manager_perms(self):
        self._test_put_object_perms()
