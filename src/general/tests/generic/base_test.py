from .base_test_setup import BaseTestCaseSetupGeneric
from .base_crud_setup import BaseCRUDTestCaseGeneric


class BaseTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseCRUDTestCaseGeneric
):
    pass
