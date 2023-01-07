from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from user.serializers import ProfileSerializer
from user.models import Profile
from user.tests.utils import create_profiles


class ProfileTestCase(APITestCase):
    """
    Test Cases for :model:`user.Profile`.
    """
    all_profiles_url = reverse('all-profiles')
    create_profile_url = reverse('create-profile')

    number_of_profiles = 4

    @classmethod
    def setUpTestData(cls):
        for index, profile in enumerate(
                create_profiles(cls.number_of_profiles),
                start=1
        ):
            setattr(cls,
                    f'profile_{index}',
                    profile
                    )

    def setUp(self) -> None:
        self.client.force_login(self.profile_1.user)

    def test_get_all_profiles(self):
        response = self.client.get(self.all_profiles_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.number_of_profiles
        )

    def test_profiles_retrieve(self):
        pk = self.profile_1.pk
        response = self.client.get(
            reverse('profile', kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['about_user'],
            self.profile_1.about_user
        )
        self.assertEqual(
            response_json,
            ProfileSerializer(self.profile_1).data
        )

    def test_profile_create(self):
        json = {
            "user": {
                "username": "string",
                "email": "user@example.com",
                "first_name": "string",
                "last_name": "string",
                "password": "string"
            },
            "about_user": "string"
        }
        response = self.client.post(
            self.create_profile_url,
            data=json,
            format='json'
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            ProfileSerializer(Profile.objects.get(pk=pk)).data
        )

    def test_delete_profile(self):
        pk = self.profile_1.pk

        response = self.client.delete(
            reverse(
                'delete-profile',
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Profile.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_profile(self):
        pk = self.profile_2.pk
        json = {
            "user": {
                "username": f'{self.profile_2.user.username}_1',
                "email": f'1{self.profile_2.user.email}',
                "first_name": self.profile_2.user.first_name,
                "last_name": self.profile_2.user.last_name,
                "password": f'{self.profile_2.user.password}'
            },
            "about_user": "123string123"
        }
        response = self.client.put(
            reverse(
                'update-profile',
                kwargs={'pk': pk}
            ),
            data=json,
            format='json'
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['about_user'],
            json['about_user'],
        )

    def test_patch_profile(self):
        pk = self.profile_2.pk
        json = {
            "about_user": "string123",
        }
        response = self.client.patch(
            reverse(
                'update-profile',
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['about_user'],
            json['about_user'],
        )
