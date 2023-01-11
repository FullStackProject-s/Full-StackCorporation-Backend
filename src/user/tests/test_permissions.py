from django.contrib.auth import get_user_model
from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import make_permission

from user.serializers import PermissionSerializer
from user.models import Permissions
from user.models.consts import StaffRole

User = get_user_model()


class PermissionsTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`user.Permissions`.
    """
    all_objects_url = reverse('all-permissions')
    create_object_url = reverse('create-permission')

    retrieve_object_url = 'permission'
    delete_object_url = 'delete-permission'

    number_of_objects = len(StaffRole.values)

    serializer_class = PermissionSerializer
    make_method = make_permission
    model_class = Permissions

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_perms(self):
        self._test_get_all_objects()

    def test_permissions_retrieve(self):
        self._test_retrieve_object()

    def test_user_create(self):
        perm = Permissions.objects.all()[0]
        role_name = perm.role_name
        perm.delete()
        json = {
            'role_name': role_name
        }
        self._test_create_object(json)

    def test_delete_permissions(self):
        self._test_delete_object()
