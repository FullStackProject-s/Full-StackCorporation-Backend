from general.tests.mixins import (
    ListObjectsMixin,
    RetrieveObjectsMixin,
    CreateObjectsMixin,
    DeleteObjectsMixin,
    UpdateObjectsMixin,

    DeleteObjectsPermsMixin,
    UpdateObjectsPermsMixin
)


class BaseCRUDURLGeneric:
    # base crud url
    all_objects_url = ''
    retrieve_object_url = ''
    delete_object_url = ''
    create_object_url = ''
    update_object_url = ''


class BaseCRUDTestCaseGeneric(
    BaseCRUDURLGeneric,
    ListObjectsMixin,
    RetrieveObjectsMixin,
    CreateObjectsMixin,
    DeleteObjectsMixin,
    UpdateObjectsMixin
):
    pass


class BaseNotSaveCRUDTestCaseGeneric(
    BaseCRUDURLGeneric,
    DeleteObjectsPermsMixin,
    UpdateObjectsPermsMixin
):
    pass
