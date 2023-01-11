from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from user.serializers import PermissionSerializer
from user.models import Permissions
from user.tests.utils import create_permissions

User = get_user_model()


class PermissionsTestCase(APITestCase):
    """
    Test Cases for :model:`user.Permissions`.
    """

    all_permissions_url = reverse('all-permissions')
    create_permission_url = reverse('create-permission')

    retrieve_permission = 'permission'
    delete_permission = 'delete-permission'

    number_of_perms = 0

    @classmethod
    def setUpTestData(cls):
        for index, perm in enumerate(
                create_permissions(),
                start=1
        ):
            cls.number_of_perms += 1
            setattr(
                cls,
                f'perm_{index}',
                perm
            )
        _keyword = 'perm'
        cls.user_perm = User.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self) -> None:
        self.client.force_login(self.user_perm)

    def test_get_all_perms(self):
        response = self.client.get(self.all_permissions_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.number_of_perms
        )

    def test_permissions_retrieve(self):
        perm = self.perm_1
        response = self.client.get(
            reverse(self.retrieve_permission, kwargs={'pk': perm.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['role_name'],
            perm.role_name
        )
        self.assertEqual(
            response_json,
            PermissionSerializer(perm).data
        )

    def test_user_create(self):
        perm = Permissions.objects.all()[0]
        role_name = perm.role_name
        perm.delete()
        json = {
            'role_name': role_name
        }
        response = self.client.post(
            self.create_permission_url,
            data=json
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            PermissionSerializer(Permissions.objects.get(pk=pk)).data
        )

    def test_delete_permissions(self):
        perm = Permissions.objects.all()[0]
        response = self.client.delete(
            reverse(self.delete_permission, kwargs={'pk': perm.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Permissions.objects.filter(pk=perm.pk).exists(),
            False
        )
