from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import make_profile, make_user

from user.models import Profile

from user.serializers import ProfileSerializer


class ProfileTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`user.Profile`.
    """
    all_objects_url = reverse('all-profiles')
    create_object_url = reverse('create-profile')

    retrieve_object_url = 'profile'
    delete_object_url = 'delete-profile'
    update_object_url = 'update-profile'

    make_method = make_profile
    model_class = Profile
    serializer_class = ProfileSerializer

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def test_get_all_profiles(self):
        self._test_get_all_objects()

    def test_profiles_retrieve(self):
        response_json = self._test_retrieve_object().json()
        self.assertEqual(
            response_json['about_user'],
            self.obj_1.about_user
        )

    def test_profile_create(self):
        user = make_user(1)
        json = {
            "user": user.pk,
            "about_user": "string"
        }
        self._test_create_object(json)

    def test_delete_profile(self):
        self._test_delete_object()

    def test_put_profile(self):
        user = make_user(1)

        json = {
            "user": user.pk,
            "about_user": "123string123"
        }
        response_json = self._test_put_object(json).json()
        self.assertEqual(
            response_json['about_user'],
            json['about_user'],
        )

    def test_patch_profile(self):
        json = {
            "about_user": "123string123"
        }
        response_json = self._test_patch_object(json).json()
        self.assertEqual(
            response_json['about_user'],
            json['about_user'],
        )
