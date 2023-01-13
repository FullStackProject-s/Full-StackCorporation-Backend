from general.tests.mixins import (
    ListObjectsMixin,
    RetrieveObjectsMixin,
    CreateObjectsMixin,
    DeleteObjectsMixin,
    UpdateObjectsMixin
)


class BaseCRUDTestCaseGeneric(
    ListObjectsMixin,
    RetrieveObjectsMixin,
    CreateObjectsMixin,
    DeleteObjectsMixin,
    UpdateObjectsMixin
):
    # base crud url
    all_objects_url = ''
    retrieve_object_url = ''
    delete_object_url = ''
    create_object_url = ''
    update_object_url = ''
