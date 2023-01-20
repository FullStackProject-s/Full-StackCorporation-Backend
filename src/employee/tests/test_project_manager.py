from django.urls import reverse

from employee.models import ProjectManager
from employee.serializers import ProjectManagerSerializer

from general.tests.generic import BaseEmployeeTestCaseGeneric
from general.tests.model_factory import (
    make_project_manager,
    make_profile
)

from user.models.consts import StaffRole


class BaseProjectManagerTestCase(BaseEmployeeTestCaseGeneric):
    """
    Test Cases for :model:`employee.ProjectManager`.
    """
    all_objects_url = reverse('all-managers')
    create_object_url = reverse('create-manager')
    obj_self_url = reverse('me-project-manager')

    retrieve_object_url = 'project-manager'
    delete_object_url = 'delete-manager'
    update_object_url = 'update-manager'

    make_method = make_project_manager
    serializer_class = ProjectManagerSerializer
    model_class = ProjectManager

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class ProjectManagerTestCase(BaseProjectManagerTestCase):
    def test_get_all_project_managers(self):
        self._test_get_all_objects()

    def test_project_manager_retrieve(self):
        self._test_retrieve_object()

    def test_project_manager_create(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }

        response_json = self._test_create_object(json).json()
        pk = response_json['pk']

        self.assertEqual(
            ProjectManager.objects.select_related(
                'profile__user'
            ).get(pk=pk).profile.user.staff_role.role_name,
            StaffRole.PRODUCT_MANAGER
        )

    def test_delete_project_manager(self):
        self._test_delete_object()

    def test_put_project_manager(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }
        response_json = self._test_put_object(json).json()

        self.assertEqual(
            response_json['team'],
            ProjectManagerSerializer(
                self.obj_1
            ).data['team']
        )

    def test_patch_project_manager(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk
        }
        self._test_patch_object(json)

    def test_me_project_manager(self):
        self._test_me(make_project_manager)
