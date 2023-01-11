from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from employee.models import Developer
from employee.serializers import DeveloperSerializer
from employee.tests.mixins import CreateUpdateEmployeeTestCaseMixin
from employee.tests.utils import create_developers
from employee.models.consts import (
    Specialty,
    SkillLevel,
)

from user.models.consts import StaffRole

User = get_user_model()


class DeveloperTestCase(
    APITestCase,
    CreateUpdateEmployeeTestCaseMixin
):
    """
    Test Cases for :model:`employee.Developers`.
    """
    all_developers_url = reverse('all-developers')
    create_developer_url = reverse('create-developer')

    retrieve_developer = 'developer'
    delete_developer = 'delete-developer'
    update_developer = 'update-developer'

    developer_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, developer in enumerate(
                create_developers(cls.developer_count),
                start=1
        ):
            setattr(
                cls,
                f'dev_{index}',
                developer
            )
        _keyword = 'developer'

        cls.login_user = User.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_developers(self):
        response = self.client.get(self.all_developers_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.developer_count
        )

    def test_developer_retrieve(self):
        dev = self.dev_1
        pk = dev.pk
        response = self.client.get(
            reverse(self.retrieve_developer, kwargs={'pk': pk})
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_json['skill_level'],
            dev.skill_level
        )
        self.assertEqual(
            response_json,
            DeveloperSerializer(dev).data
        )
        self.assertEqual(
            dev.profile.user.staff_role.role_name,
            StaffRole.DEVELOPER
        )

    def test_developer_create(self):
        response = self._create_employee_response(
            self.developer_count,
            self.create_developer_url,
            skill_level=SkillLevel.senior
        )

        response_json = response.json()
        pk = response_json['pk']

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            DeveloperSerializer(
                Developer.objects.get(pk=pk)
            ).data
        )

    def test_delete_developer(self):
        pk = self.dev_1.pk

        response = self.client.delete(
            reverse(
                self.delete_developer,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Developer.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_developer(self):
        pk = self.dev_2.pk
        response = self._put_employee_response(
            self.developer_count,
            reverse(
                self.update_developer,
                kwargs={'pk': pk}
            ),
            skill_level=SkillLevel.senior
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['skill_level'],
            SkillLevel.senior
        )

    def test_patch_developer(self):
        dev = self.dev_2
        response = self._patch_employee_response(
            self.developer_count,
            reverse(
                self.update_developer,
                kwargs={'pk': dev.pk}
            ),
            specialty=Specialty.FRONT,

        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertNotEqual(
            response_json['profile'],
            dev.profile.pk
        )
