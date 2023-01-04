from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class CustomUserTestCase(APITestCase):
    """
    Test Cases for :model:`user.CustomUser`.
    """
    all_users_url = reverse('all-users')
    user_url = reverse('user', kwargs={'pk': 2})
    create_user_url = reverse('create-user')
    delete_user_url = reverse('delete-user', kwargs={'pk': 1})
    update_user_url = reverse('update-user', kwargs={'pk': 2})

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
        self.assertEqual(
            response.json()['username'],
            self.user_2.username
        )
