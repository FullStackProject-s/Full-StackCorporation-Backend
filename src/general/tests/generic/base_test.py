from .base_test_setup import (
    BaseTestCaseSetupGeneric,
    BaseTestCaseSetupPermissionsGeneric, BaseEmployeeTestCaseSetupGeneric
)
from .base_crud_setup import (
    BaseCRUDTestCaseGeneric,
    BaseNotSaveCRUDTestCaseGeneric,
    BaseEmployeeCRUDTestCaseGeneric
)


class BaseTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseCRUDTestCaseGeneric
):
    pass


class BaseTestCasePermissionsGeneric(
    BaseTestCaseSetupPermissionsGeneric,
    BaseNotSaveCRUDTestCaseGeneric
):
    pass


class BaseEmployeeTestCaseGeneric(
    BaseEmployeeTestCaseSetupGeneric,
    BaseEmployeeCRUDTestCaseGeneric
):
    pass
