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

    # tested serializer
    serializer_class = None
    # tested model
    model_class = None
    # default picker object number, obj_1
    default_object_number = 1
