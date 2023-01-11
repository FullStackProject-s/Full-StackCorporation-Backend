from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from user.serializers import ProfileSerializer
from user.models import Profile
from user.tests.utils import create_profiles, create_users_list


class ProfileTestCase(APITestCase):
    """
    Test Cases for :model:`user.Profile`.
    """
    all_profiles_url = reverse('all-profiles')
    create_profile_url = reverse('create-profile')

    retrieve_profile = 'profile'
    delete_profile = 'delete-profile'
    update_profile = 'update-profile'

    number_of_profiles = 4

    @classmethod
    def setUpTestData(cls):
        for index, profile in enumerate(
                create_profiles(cls.number_of_profiles),
                start=1
        ):
            setattr(
                cls,
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
        profile = self.profile_1
        pk = profile.pk
        response = self.client.get(
            reverse(self.retrieve_profile, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()
        self.assertEqual(
            response_json['about_user'],
            profile.about_user
        )
        self.assertEqual(
            response_json,
            ProfileSerializer(profile).data
        )

    def test_profile_create(self):
        start = abs(hash('test_profile_create'))
        user = create_users_list(start, start=start)[0]

        Profile.objects.get(user=user).delete()
        json = {
            "user": user.pk,
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
                self.delete_profile,
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
        start = abs(hash('test_put_profile'))
        user = create_users_list(start, start=start)[0]

        Profile.objects.get(user=user).delete()

        profile = self.profile_2
        pk = profile.pk
        json = {
            "user": user.pk,
            "about_user": "123string123"
        }
        response = self.client.put(
            reverse(
                self.update_profile,
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
        self.assertEqual(
            response_json,
            ProfileSerializer(Profile.objects.get(pk=pk)).data
        )

    def test_patch_profile(self):
        pk = self.profile_2.pk
        json = {
            "about_user": "string123",
        }
        response = self.client.patch(
            reverse(
                self.update_profile,
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
