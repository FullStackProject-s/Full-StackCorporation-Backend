from django.test import override_settings

from .base_test_setup import BaseTestCaseSetupGeneric
from .base_crud_setup import BaseCRUDTestCaseGeneric


# By default, all signals with special decorator disable when test run
@override_settings(SUSPEND_SIGNALS=True)
class BaseTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseCRUDTestCaseGeneric
):
    pass
