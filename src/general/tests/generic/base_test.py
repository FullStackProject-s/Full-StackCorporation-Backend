from django.test import override_settings

from .base_test_setup import BaseTestCaseSetupGeneric
from .base_crud_setup import BaseCRUDTestCaseGeneric


@override_settings(SUSPEND_SIGNALS=False)
class BaseTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseCRUDTestCaseGeneric
):
    pass
