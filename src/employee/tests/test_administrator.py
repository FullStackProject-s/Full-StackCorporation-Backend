from django.urls import reverse

from employee.models import Administrator
from employee.serializers import AdministratorSerializer

from general.tests.generic import BaseEmployeeTestCaseGeneric

from general.tests.model_factory import (
    make_profile,
    make_administrator
)

from user.models.consts import StaffRole


class BaseAdministratorTestCase(BaseEmployeeTestCaseGeneric):
    """
    Test Cases for :model:`employee.Administrator`.
    """
    all_objects_url = reverse('all-admins')
    create_object_url = reverse('create-admin')
    obj_self_url = reverse('me-admin')

    retrieve_object_url = 'admin'
    delete_object_url = 'delete-admin'
    update_object_url = 'update-admin'

    make_method = make_administrator
    serializer_class = AdministratorSerializer
    model_class = Administrator

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class AdministratorTestCase(BaseAdministratorTestCase):
    def test_get_all_admins(self):
        self._test_get_all_objects()

    def test_admin_retrieve(self):
        self._test_retrieve_object()

    def test_admins_create(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }
        response_json = self._test_create_object(json).json()
        pk = response_json['pk']

        self.assertEqual(
            Administrator.objects.select_related(
                'profile__user'
            ).get(pk=pk).profile.user.staff_role.role_name,
            StaffRole.ADMIN
        )

    def test_delete_admin(self):
        self._test_delete_object()

    def test_put_admin(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }
        self._test_put_object(json)

    def test_patch_admin(self):
        admin = self.obj_2
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }
        response_json = self._test_patch_object(json).json()
        self.assertNotEqual(
            response_json['profile'],
            admin.profile.pk
        )

    def test_me_admin(self):
        self._test_me(make_administrator)
