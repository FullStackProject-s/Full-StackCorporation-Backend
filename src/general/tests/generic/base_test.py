from django.test import override_settings

from .base_test_setup import (
    BaseTestCaseSetupGeneric,
    BaseTestCaseSetupPermissionsGeneric
)
from .base_crud_setup import (
    BaseCRUDTestCaseGeneric,
    BaseNotSaveCRUDTestCaseGeneric
)


@override_settings(TESTS_LAUNCHED=True)
class BaseTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseCRUDTestCaseGeneric
):
    pass


@override_settings(TESTS_LAUNCHED=True)
class BaseTestCasePermissionsGeneric(
    BaseTestCaseSetupPermissionsGeneric,
    BaseNotSaveCRUDTestCaseGeneric
):
    pass
