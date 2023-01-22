from .base_test_setup import (
    BaseTestCaseSetupGeneric,
    BaseTestCaseSetupPermissionsGeneric
)
from .base_crud_setup import (
    BaseCRUDTestCaseGeneric,
    BaseNotSaveCRUDTestCaseGeneric,
    BaseEmployeeCRUDTestCaseGeneric,
    BaseUploadFileURLTestCaseGeneric
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
    BaseTestCaseSetupGeneric,
    BaseEmployeeCRUDTestCaseGeneric
):
    pass


class BaseUploadFileTestCaseGeneric(
    BaseTestCaseSetupGeneric,
    BaseUploadFileURLTestCaseGeneric,
):
    pass
