from django.urls import reverse

from employee.models import DeveloperOrganizationSpecialty
from employee.models.consts import Specialty
from employee.serializers import DeveloperOrgSpecialtySerializer

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import make_specialty


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

    # def test_speciality_create(self):
    #     orgs_start = abs(hash('test_speciality_create_orgs'))
    #     devs_start = abs(hash('test_speciality_create_devs'))
    #     dev = create_developers(devs_start, start=devs_start)[0]
    #     org = create_organizations(orgs_start, start=orgs_start)[0]
    #
    #     json = {
    #         "specialty": Specialty.FRONT,
    #         "organization_developer": dev.pk,
    #         "organization": org.pk
    #     }
    #     response = self.client.post(
    #         self.create_spec_url,
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
    #         DeveloperOrgSpecialtySerializer(
    #             DeveloperOrganizationSpecialty.objects.get(
    #                 pk=pk
    #             )
    #         ).data
    #     )
    #
    #     # test signal
    #     self.assertIn(
    #         DeveloperOrganizationSpecialty.objects.get(pk=pk),
    #         Developer.objects.get(pk=dev.pk).specialties.all(),
    #     )
    #
    # def test_delete_speciality(self):
    #     pk = self.spec_1.pk
    #
    #     response = self.client.delete(
    #         reverse(
    #             self.delete_speciality,
    #             kwargs={'pk': pk}
    #         )
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_204_NO_CONTENT
    #     )
    #     self.assertEqual(
    #         DeveloperOrganizationSpecialty.objects.filter(pk=pk).exists(),
    #         False
    #     )
    #
    # def test_put_speciality(self):
    #     spec = self.spec_2
    #     orgs_start = abs(hash('test_put_technologies_orgs'))
    #     devs_start = abs(hash('test_put_technologies_devs'))
    #
    #     dev = create_developers(devs_start, start=devs_start)[0]
    #     org = create_organizations(orgs_start, start=orgs_start)[0]
    #
    #     pk = spec.pk
    #     json = {
    #         "specialty": Specialty.BACK,
    #         "organization_developer": dev.pk,
    #         "organization": org.pk
    #     }
    #     response = self.client.put(
    #         reverse(
    #             self.update_speciality,
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
    #         response_json['specialty'],
    #         json['specialty'],
    #     )
    #
    # def test_patch_speciality(self):
    #     spec = self.spec_2
    #
    #     pk = spec.pk
    #     json = {
    #         "specialty": Specialty.DEVOPS,
    #     }
    #     response = self.client.patch(
    #         reverse(
    #             self.update_speciality,
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
    #         response_json['specialty'],
    #         json['specialty'],
    #     )
