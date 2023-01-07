from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from user.serializers import CustomUserSerializer
from user.models import CustomUser

User = get_user_model()


class CustomUserTestCase(APITestCase):
    """
    Test Cases for :model:`user.CustomUser`.
    """
    delete_user_pk = 1
    update_user_pk = 2
    all_users_url = reverse('all-users')
    user_url = reverse('user', kwargs={'pk': 2})
    create_user_url = reverse('create-user')
    delete_user_url = reverse('delete-user', kwargs={'pk': delete_user_pk})
    update_user_url = reverse('update-user', kwargs={'pk': update_user_pk})

    number_of_users = 4

    @classmethod
    def setUpTestData(cls):
        for i in range(1, cls.number_of_users + 1):
            user = User.objects.create_user(
                username=f'user_{i}',
                email=f'user{i}@example.com',
                password=f'user_{i}',
                first_name=f'first_{i}',
                last_name=f'last_{i}',
            )
            setattr(cls,
                    f'user_{i}',
                    user
                    )

    def setUp(self) -> None:
        self.client.force_login(self.user_1)

    def test_get_all_users(self):
        response = self.client.get(self.all_users_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.number_of_users
        )

    def test_user_retrieve(self):
        response = self.client.get(self.user_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['username'],
            self.user_2.username
        )
        self.assertEqual(
            response_json,
            CustomUserSerializer(self.user_2).data
        )

    def test_user_create(self):
        json = {
            'username': "create_user",
            'email': 'create@user.com',
            'first_name': "create_first",
            "last_name": "create_last",
            "password": "123"
        }
        response = self.client.post(
            self.create_user_url,
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
            CustomUserSerializer(CustomUser.objects.get(pk=pk)).data
        )

    def test_delete_user(self):
        response = self.client.delete(
            self.delete_user_url
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            CustomUser.objects.filter(pk=self.delete_user_pk).exists(),
            False
        )

    def test_put_user(self):
        json = {
            'username': f'user_{self.update_user_pk}',
            'email': f'user{self.update_user_pk}@example.com',
            'password': f'user_{self.update_user_pk}',
            'first_name': f'first_{self.update_user_pk}',
            'last_name': f'second_{self.update_user_pk}',
        }
        response = self.client.put(
            self.update_user_url,
            data=json
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['last_name'],
            json['last_name'],
        )

    def test_patch_user(self):
        json = {
            'first_name': f'first_{self.update_user_pk}',
        }
        response = self.client.patch(
            self.update_user_url,
            data=json
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['first_name'],
            json['first_name'],
        )