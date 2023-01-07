from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from user.models import Profile
from user.tests.utils import create_profiles
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileTestCase(APITestCase):
    """
    Test Cases for :model:`user.Profile`.
    """
    delete_profile_pk = 1
    update_profile_pk = 2
    all_profiles_url = reverse('all-profiles')
    user_url = reverse('profile', kwargs={'pk': 2})
    create_profile_url = reverse('create-profile')
    delete_profile_url = reverse(
        'delete-profile',
        kwargs={'pk': delete_profile_pk}
    )
    update_profile_url = reverse(
        'update-profile',
        kwargs={'pk': update_profile_pk}
    )

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
        print(User.objects.all())

        # cls.user_1 = User.objects.create_user(
        #     username=f'user_1',
        #     email=f'user1@example.com',
        #     password=f'user_1',
        #     first_name=f'first_1',
        #     last_name=f'last_1'
        # )

#     def setUp(self) -> None:
#         self.client.force_login(self.user_1)
#
    def test_get_all_users(self):
        # print(User.objects.all())
        pass
        # response = self.client.get(self.all_profiles_url)

#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#         self.assertEqual(
#             len(response.json()),
#             self.number_of_profiles
#         )

    # def test_user_retrieve(self):
    #     response = self.client.get(self.user_url)
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     response_json = response.json()
    #     self.assertEqual(
    #         response_json['username'],
    #         self.user_2.username
    #     )
    #     self.assertEqual(
    #         response_json,
    #         CustomUserSerializer(self.user_2).data
    #     )
    #
    # def test_user_create(self):
    #     json = {
    #         'username': "create_user",
    #         'email': 'create@user.com',
    #         'first_name': "create_first",
    #         "last_name": "create_last",
    #         "password": "123"
    #     }
    #     response = self.client.post(
    #         self.create_user_url,
    #         data=json
    #     )
    #     response_json = response.json()
    #     pk = response_json['pk']
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )
    #     self.assertEqual(
    #         response_json,
    #         CustomUserSerializer(CustomUser.objects.get(pk=pk)).data
    #     )
    #
    # def test_delete_user(self):
    #     response = self.client.delete(
    #         self.delete_user_url
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_204_NO_CONTENT
    #     )
    #     self.assertEqual(
    #         CustomUser.objects.filter(pk=self.delete_user_pk).exists(),
    #         False
    #     )
    #
    # def test_put_user(self):
    #     json = {
    #         'username': f'user_{self.update_user_pk}',
    #         'email': f'user{self.update_user_pk}@example.com',
    #         'password': f'user_{self.update_user_pk}',
    #         'first_name': f'first_{self.update_user_pk}',
    #         'last_name': f'second_{self.update_user_pk}',
    #     }
    #     response = self.client.put(
    #         self.update_user_url,
    #         data=json
    #     )
    #     response_json = response.json()
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response_json['last_name'],
    #         json['last_name'],
    #     )
    #
    # def test_patch_user(self):
    #     json = {
    #         'first_name': f'first_{self.update_user_pk}',
    #     }
    #     response = self.client.patch(
    #         self.update_user_url,
    #         data=json
    #     )
    #     response_json = response.json()
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response_json['first_name'],
    #         json['first_name'],
    #     )
