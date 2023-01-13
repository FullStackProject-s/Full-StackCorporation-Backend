from django.urls import reverse

from employee.models import Developer
from employee.serializers import DeveloperSerializer
from employee.models.consts import SkillLevel

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import (
    make_developer,
    make_profile
)

from user.models.consts import StaffRole


class DeveloperTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`employee.Developers`.
    """
    all_objects_url = reverse('all-developers')
    create_object_url = reverse('create-developer')

    retrieve_object_url = 'developer'
    delete_object_url = 'delete-developer'
    update_object_url = 'update-developer'

    make_method = make_developer
    serializer_class = DeveloperSerializer
    model_class = Developer

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_developers(self):
        self._test_get_all_objects()

    def test_developer_retrieve(self):
        dev = self.obj_1

        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['skill_level'],
            dev.skill_level
        )

    def test_developer_create(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk,
            'skill_level': SkillLevel.senior
        }

        response_json = self._test_create_object(json).json()
        pk = response_json['pk']
        self.assertEqual(
            response_json['skill_level'],
            SkillLevel.senior
        )
        self.assertEqual(
            Developer.objects.select_related(
                'profile__user'
            ).get(pk=pk).profile.user.staff_role.role_name,
            StaffRole.DEVELOPER
        )

    def test_delete_developer(self):
        self._test_delete_object()

    def test_put_developer(self):
        profile = make_profile(1)
        json = {
            'profile': profile.pk,
            'skill_level': SkillLevel.senior
        }
        self.default_object_number = 2
        response_json = self._test_put_object(json).json()
        self.assertEqual(
            response_json['skill_level'],
            SkillLevel.senior
        )

    def test_patch_developer(self):
        profile = make_profile(1)
        dev = self.obj_2
        self.default_object_number = 2
        json = {
            'profile': profile.pk,
            'skill_level': SkillLevel.junior,
        }
        response_json = self._test_patch_object(json).json()
        self.assertNotEqual(
            response_json['profile'],
            dev.profile.pk
        )
