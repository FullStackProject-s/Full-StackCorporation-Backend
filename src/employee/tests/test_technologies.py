from django.urls import reverse

from rest_framework import status

from employee.models import Technologies
from employee.serializers import TechnologiesSerializer
from employee.tests.utils import create_technologies
from employee.models.consts import TechnologiesStack

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import make_technologies


class TechnologiesTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`employee.Technologies`.
    """
    all_objects_url = reverse('all-tech')
    create_object_url = reverse('create-tech')

    retrieve_object_url = 'technology'
    delete_object_url = 'delete-tech'
    update_object_url = 'update-tech'

    make_method = make_technologies
    serializer_class = TechnologiesSerializer
    model_class = Technologies

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_technologies(self):
        self._test_get_all_objects()

    def test_technologies_retrieve(self):
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['technology_name'],
            self.obj_1.technology_name
        )

    def test_technologies_create(self):
        json = {
            "technology_name": f'tech_create',
            "technology_category": TechnologiesStack.FRONT
        }
        self._test_create_object(json)

    def test_delete_technologies(self):
        self._test_delete_object()

    def test_put_technologies(self):
        self.default_object_number = 2
        json = {
            "technology_name": f'test_put_technologies_2',
            "technology_category": TechnologiesStack.FRONT
        }

        response_json = self._test_put_object(json).json()
        self.assertEqual(
            response_json['technology_name'],
            json['technology_name'],
        )

    def test_patch_technologies(self):
        json = {
            "technology_name": 'test_patch_technologies'
        }
        response_json = self._test_patch_object(json).json()
        self.assertEqual(
            response_json['technology_name'],
            json['technology_name'],
        )
