from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from employee.models import ProjectManager
from employee.tests.mixins import CreateUpdateEmployeeTestCaseMixin
from employee.tests.utils import create_project_managers
from employee.serializers import ProjectManagerSerializer

User = get_user_model()


class ProjectManagerTestCase(
    APITestCase,
    CreateUpdateEmployeeTestCaseMixin
):
    """
    Test Cases for :model:`employee.ProjectManager`.
    """
    all_project_managers_url = reverse('all-managers')
    create_project_manager_url = reverse('create-manager')

    retrieve_project_manager = 'project-manager'
    delete_project_manager = 'delete-manager'
    update_project_manager = 'update-manager'

    project_manager_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, project_manager in enumerate(
                create_project_managers(cls.project_manager_count),
                start=1
        ):
            setattr(cls,
                    f'proj_manager_{index}',
                    project_manager
                    )
        _keyword = 'project_manager'

        cls.login_user = User.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_project_managers(self):
        response = self.client.get(self.all_project_managers_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.project_manager_count
        )

    def test_project_manager_retrieve(self):
        proj_manager = self.proj_manager_1
        pk = proj_manager.pk
        response = self.client.get(
            reverse(self.retrieve_project_manager, kwargs={'pk': pk})
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['team'],
            None
        )
        self.assertEqual(
            response_json,
            ProjectManagerSerializer(proj_manager).data
        )

    def test_project_manager_create(self):
        response = self._create_employee_response(
            self.project_manager_count,
            self.create_project_manager_url
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            ProjectManager.objects.filter(pk=pk).exists(),
            True
        )

    def test_delete_project_manager(self):
        pk = self.proj_manager_1.pk

        response = self.client.delete(
            reverse(
                self.delete_project_manager,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            ProjectManager.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_project_manager(self):
        proj_manager = self.proj_manager_2

        response = self._put_employee_response(
            self.project_manager_count,
            reverse(
                self.update_project_manager,
                kwargs={'pk': proj_manager.pk}
            ),
            keyword='test_put_project_manager'
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['team'],
            ProjectManagerSerializer(
                proj_manager
            ).data['team']
        )

    def test_patch_project_manager(self):
        proj_manager = self.proj_manager_2
        response = self._patch_employee_response(
            self.project_manager_count,
            reverse(
                self.update_project_manager,
                kwargs={'pk': proj_manager.pk}
            ),
            keyword='test_patch_project_manager'
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['pk'],
            proj_manager.pk
        )
