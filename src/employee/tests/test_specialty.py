from django.urls import reverse

from employee.models import DeveloperOrganizationSpecialty, Developer
from employee.models.consts import Specialty
from employee.serializers import DeveloperOrgSpecialtySerializer

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import (
    make_specialty,
    make_developer,
    make_organization
)


class DeveloperOrganizationSpecialtyTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`employee.DeveloperOrganizationSpecialty`.
    """
    all_objects_url = reverse('all-specialities')
    create_object_url = reverse('create-speciality')

    retrieve_object_url = 'speciality'
    delete_object_url = 'delete-speciality'
    update_object_url = 'update-speciality'

    number_of_objects = len(Specialty.values)

    make_method = make_specialty
    serializer_class = DeveloperOrgSpecialtySerializer
    model_class = DeveloperOrganizationSpecialty

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_specialities(self):
        self._test_get_all_objects()

    def test_speciality_retrieve(self):
        spec = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['specialty'],
            spec.specialty
        )

    def test_speciality_create(self):
        dev = make_developer(1)
        org = make_organization(1)

        json = {
            "specialty": Specialty.FRONT,
            "organization_developer": dev.pk,
            "organization": org.pk
        }

        response_json = self._test_create_object(json).json()
        pk = response_json['pk']

        self.assertIn(
            DeveloperOrganizationSpecialty.objects.get(pk=pk),
            Developer.objects.get(pk=dev.pk).specialties.all(),
        )

    def test_delete_speciality(self):
        self._test_delete_object()

    def test_put_speciality(self):
        self.default_object_number = 2

        dev = make_developer(1)
        org = make_organization(1)

        json = {
            "specialty": Specialty.BACK,
            "organization_developer": dev.pk,
            "organization": org.pk
        }
        response_json = self._test_put_object(json).json()

        self.assertEqual(
            response_json['specialty'],
            json['specialty'],
        )

    def test_patch_speciality(self):
        self.default_object_number = 2
        json = {
            "specialty": Specialty.DEVOPS,
        }

        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            response_json['specialty'],
            json['specialty'],
        )
