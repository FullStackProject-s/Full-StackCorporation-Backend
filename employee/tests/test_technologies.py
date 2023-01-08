from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from employee.models import Technologies
from employee.serializers import TechnologiesSerializer
from employee.tests.utils import create_technologies
from employee.models.consts import TechnologiesStack

from user.models import CustomUser


class TechnologiesTestCase(APITestCase):
    """
    Test Cases for :model:`employee.Technologies`.
    """
    all_tech_url = reverse('all-tech')
    create_tech_url = reverse('create-tech')

    retrieve_tech = 'technology'
    delete_tech = 'delete-tech'
    update_tech = 'update-tech'

    count_all_tech = 0

    @classmethod
    def setUpTestData(cls):
        for index, tech in enumerate(
                create_technologies(start=1),
                start=1
        ):
            cls.count_all_tech += 1
            setattr(cls,
                    f'tech_{index}',
                    tech
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
            reverse(self.retrieve_tech, kwargs={'pk': pk})
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
            "technology_name": f'tech_create',
            "technology_category": TechnologiesStack.FRONT
        }
        response = self.client.post(
            self.create_tech_url,
            data=json
        )
        response_json = response.json()
        name = response_json['technology_name']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            TechnologiesSerializer(
                Technologies.objects.get(technology_name=name)
            ).data
        )

    def test_delete_technologies(self):
        pk = self.tech_1.pk

        response = self.client.delete(
            reverse(
                self.delete_tech,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Technologies.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_technologies(self):
        pk = self.tech_2.pk
        json = {
            "technology_name": f'{self.tech_2}_2',
            "technology_category": TechnologiesStack.FRONT
        }
        response = self.client.put(
            reverse(
                self.update_tech,
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
            response_json['technology_name'],
            json['technology_name'],
        )

    def test_patch_profile(self):
        pk = self.tech_2.pk
        json = {
            "technology_category": TechnologiesStack.FRONT
        }
        response = self.client.patch(
            reverse(
                self.update_tech,
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
            response_json['technology_category'],
            json['technology_category'],
        )
