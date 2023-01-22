from general.tests.mixins import (
    ListObjectsMixin,
    RetrieveObjectsMixin,
    CreateObjectsMixin,
    DeleteObjectsMixin,
    UpdateObjectsMixin,

    DeleteObjectsPermsMixin,
    UpdateObjectsPermsMixin,

    TestMeEndpointMixin,
    ImageUploadMixin
)


class BaseCRUDURLGeneric:
    # base crud url
    all_objects_url = ''
    retrieve_object_url = ''
    delete_object_url = ''
    create_object_url = ''
    update_object_url = ''


class BaseUploadFileURLGeneric:
    upload_obj_image_url = ''


class BaseUploadFileURLTestCaseGeneric(
    BaseUploadFileURLGeneric,
    ImageUploadMixin
):
    pass


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


class BaseEmployeeCRUDTestCaseGeneric(
    BaseCRUDTestCaseGeneric,
    TestMeEndpointMixin
):
    obj_self_url = ''
