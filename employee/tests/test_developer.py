from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


from employee.models import Developer
from employee.serializers import DeveloperSerializer
from employee.tests.mixins import CreateUpdateEmployeeTestCaseMixin
from employee.tests.utils import create_developers, create_technologies
from employee.models.consts import (
    Specialty,
    SkillLevel,
    TechnologiesStack
)

from user.models import CustomUser


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
    add_developer_tech = 'add-developer-tech'
    remove_developer_tech = 'remove-developer-tech'

    developer_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, developer in enumerate(
                create_developers(cls.developer_count),
                start=1
        ):
            setattr(cls,
                    f'dev_{index}',
                    developer
                    )
        _keyword = 'developer'

        cls.login_user = CustomUser.objects.create_user(
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
            response_json['specialty'],
            dev.specialty
        )
        self.assertEqual(
            response_json['skill_level'],
            dev.skill_level
        )
        self.assertEqual(
            response_json,
            DeveloperSerializer(dev).data
        )

    def test_developer_create(self):
        response = self._create_employee_response(
            self.developer_count,
            self.create_developer_url,
            specialty=Specialty.FULLSTACK,
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

    def test_put_project_manager(self):
        pk = self.dev_2.pk
        response = self._put_employee_response(
            self.developer_count,
            reverse(
                self.update_developer,
                kwargs={'pk': pk}
            ),
            specialty=Specialty.FULLSTACK,
            skill_level=SkillLevel.senior
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['specialty'],
            Specialty.FULLSTACK
        )
        self.assertEqual(
            response_json['skill_level'],
            SkillLevel.senior
        )

    def test_patch_project_manager(self):
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
        self.assertNotEqual(
            response_json['specialty'],
            Specialty.FRONT.name
        )

    def test_add_technologies_to_developer(self):
        dev = self.dev_2
        pk = dev.pk

        start = self.developer_count + abs(
            hash('add_technologies_to_developer')
        )
        technologies_name_list = list(map(
            lambda x: x.technology_name,
            create_technologies(start=start)
        ))
        json = {
            'technology_names': technologies_name_list
        }
        response = self.client.post(
            reverse(
                self.add_developer_tech,
                kwargs={'pk': pk},
            ),
            data=json

        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            [tech['technology_name']
             for tech in Developer.objects.get(pk=pk).stack.values()
             ],
            technologies_name_list
        )

    def test_remove_technologies_to_developer(self):
        dev = self.dev_2
        start = self.developer_count + abs(
            hash('remove_technologies_to_developer')
        )
        technologies_list = create_technologies(start=start)
        for tech in technologies_list:
            dev.append_technologies(tech)

        technologies_name_list = list(map(
            lambda x: x.technology_name,
            technologies_list
        ))
        tech_rem_list = technologies_name_list[0:(len(TechnologiesStack) // 2)]

        pk = dev.pk
        json = {
            'technology_names': tech_rem_list
        }
        response = self.client.post(
            reverse(
                self.remove_developer_tech,
                kwargs={'pk': pk},
            ),
            data=json

        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        for tech_names in [
            tech['technology_name']
            for tech in Developer.objects.get(pk=pk).stack.values()
        ]:
            self.assertEqual(
                tech_names not in tech_rem_list,
                True
            )
