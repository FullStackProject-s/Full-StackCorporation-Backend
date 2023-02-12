from django.urls import reverse

from rest_framework import status

from general.tests.generic import (
    BaseTestCaseGeneric,
    BaseUploadFileTestCaseGeneric
)
from general.tests.model_factory import (
    make_profile,
    make_user
)

from user.models import Profile
from user.serializers import ProfileSerializer


class BaseProfileTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`user.Profile`.
    """
    all_objects_url = reverse('all-profiles')
    create_object_url = reverse('create-profile')
    obj_self_url = reverse('me-profile')

    retrieve_object_url = 'profile'
    delete_object_url = 'delete-profile'
    update_object_url = 'update-profile'

    make_method = make_profile
    model_class = Profile
    serializer_class = ProfileSerializer

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class ProfileTestCase(BaseProfileTestCase):
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

    def test_get_self_user(self):
        profile = make_profile(1)

        user = profile.user
        user.is_active = True
        user.save()

        self.client.force_login(user)
        self._set_credentials_for_user(user)

        response = self.client.get(self.obj_self_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            self.serializer_class(profile).data
        )


class ProfileUploadFileTestCaseGeneric(
    BaseUploadFileTestCaseGeneric,
    BaseProfileTestCase,
):
    upload_obj_image_url = 'upload-profile-image'

    def test_upload_profile_image(self):
        self._test_image_upload('profile_avatar')
        self.model_class.objects.get(
            pk=self.obj_1.pk
        ).profile_avatar.delete()
