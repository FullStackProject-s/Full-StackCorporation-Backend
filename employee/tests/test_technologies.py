from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from employee.serializers import TechnologiesSerializer
from employee.tests.utils import create_technologies
from user.models import CustomUser


class TechnologiesTestCase(APITestCase):
    """
    Test Cases for :model:`employee.Technologies`.
    """
    all_tech_url = reverse('all-tech')
    create_profile_url = reverse('create-profile')
    count_all_tech = 0

    @classmethod
    def setUpTestData(cls):
        for index, profile in enumerate(
                create_technologies(),
                start=1
        ):
            cls.count_all_tech += 1
            setattr(cls,
                    f'tech_{index}',
                    profile
                    )
        _keyword = 'technologies'

        cls.login_user = CustomUser.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_technologies(self):
        response = self.client.get(self.all_tech_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.count_all_tech
        )

    def test_technologies_retrieve(self):
        pk = self.tech_1.pk
        response = self.client.get(
            reverse('technology', kwargs={'pk': pk})
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['technology_name'],
            self.tech_1.technology_name
        )
        self.assertEqual(
            response_json,
            TechnologiesSerializer(self.tech_1).data
        )

    def test_technologies_create(self):
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

    # def test_delete_profile(self):
    #     pk = self.profile_1.pk
    #
    #     response = self.client.delete(
    #         reverse(
    #             'delete-profile',
    #             kwargs={'pk': pk}
    #         )
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_204_NO_CONTENT
    #     )
    #     self.assertEqual(
    #         Profile.objects.filter(pk=pk).exists(),
    #         False
    #     )
    #
    # def test_put_profile(self):
    #     pk = self.profile_2.pk
    #     json = {
    #         "user": {
    #             "username": f'{self.profile_2.user.username}_1',
    #             "email": f'1{self.profile_2.user.email}',
    #             "first_name": self.profile_2.user.first_name,
    #             "last_name": self.profile_2.user.last_name,
    #             "password": f'{self.profile_2.user.password}'
    #         },
    #         "about_user": "123string123"
    #     }
    #     response = self.client.put(
    #         reverse(
    #             'update-profile',
    #             kwargs={'pk': pk}
    #         ),
    #         data=json,
    #         format='json'
    #     )
    #     response_json = response.json()
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response_json['about_user'],
    #         json['about_user'],
    #     )
    #
    # def test_patch_profile(self):
    #     pk = self.profile_2.pk
    #     json = {
    #         "about_user": "string123",
    #     }
    #     response = self.client.patch(
    #         reverse(
    #             'update-profile',
    #             kwargs={'pk': pk}
    #         ),
    #         data=json
    #     )
    #     response_json = response.json()
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response_json['about_user'],
    #         json['about_user'],
    #     )
