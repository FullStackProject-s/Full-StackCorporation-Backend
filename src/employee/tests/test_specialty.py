from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from employee.models import DeveloperOrganizationSpecialty, Developer
from employee.tests.utils import create_specialities, create_developers
from employee.models.consts import Specialty
from employee.serializers import DeveloperOrgSpecialtySerializer

from organization.tests.utils import create_organizations

User = get_user_model()


class DeveloperOrganizationSpecialtyTestCase(APITestCase):
    """
    Test Cases for :model:`employee.DeveloperOrganizationSpecialty`.
    """
    all_spec_url = reverse('all-specialities')
    create_spec_url = reverse('create-speciality')

    retrieve_speciality = 'speciality'
    delete_speciality = 'delete-speciality'
    update_speciality = 'update-speciality'

    count_all_spec = 4

    @classmethod
    def setUpTestData(cls):
        for index, spec in enumerate(
                create_specialities(cls.count_all_spec, start=1),
                start=1
        ):
            setattr(
                cls,
                f'spec_{index}',
                spec
            )
        _keyword = 'speciality'

        cls.login_user = User.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_specialities(self):
        response = self.client.get(self.all_spec_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.count_all_spec
        )

    def test_speciality_retrieve(self):
        spec = self.spec_1
        pk = spec.pk
        response = self.client.get(
            reverse(self.retrieve_speciality, kwargs={'pk': pk})
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['specialty'],
            spec.specialty
        )
        self.assertEqual(
            response_json,
            DeveloperOrgSpecialtySerializer(spec).data
        )

    def test_speciality_create(self):
        orgs_start = abs(hash('test_speciality_create_orgs'))
        devs_start = abs(hash('test_speciality_create_devs'))
        dev = create_developers(devs_start, start=devs_start)[0]
        org = create_organizations(orgs_start, start=orgs_start)[0]

        json = {
            "specialty": Specialty.FRONT,
            "organization_developer": dev.pk,
            "organization": org.pk
        }
        response = self.client.post(
            self.create_spec_url,
            data=json
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            DeveloperOrgSpecialtySerializer(
                DeveloperOrganizationSpecialty.objects.get(
                    pk=pk
                )
            ).data
        )

        # test signal
        self.assertIn(
            DeveloperOrganizationSpecialty.objects.get(pk=pk),
            Developer.objects.get(pk=dev.pk).specialties.all(),
        )

    def test_delete_speciality(self):
        pk = self.spec_1.pk

        response = self.client.delete(
            reverse(
                self.delete_speciality,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            DeveloperOrganizationSpecialty.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_speciality(self):
        spec = self.spec_2
        orgs_start = abs(hash('test_put_technologies_orgs'))
        devs_start = abs(hash('test_put_technologies_devs'))

        dev = create_developers(devs_start, start=devs_start)[0]
        org = create_organizations(orgs_start, start=orgs_start)[0]

        pk = spec.pk
        json = {
            "specialty": Specialty.BACK,
            "organization_developer": dev.pk,
            "organization": org.pk
        }
        response = self.client.put(
            reverse(
                self.update_speciality,
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
            response_json['specialty'],
            json['specialty'],
        )

    def test_patch_speciality(self):
        spec = self.spec_2

        pk = spec.pk
        json = {
            "specialty": Specialty.DEVOPS,
        }
        response = self.client.patch(
            reverse(
                self.update_speciality,
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
            response_json['specialty'],
            json['specialty'],
        )
