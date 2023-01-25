from django.conf import settings

from general.tests.generic import BaseTestCaseGeneric
from general.models.utils import set_image_on_imagefield
from general.tests.model_factory import make_profile

from user.models import Profile


class TestImageSetAvatarUnit(BaseTestCaseGeneric):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_set_avatar(self):
        settings.TESTS_LAUNCHED = False

        profile = make_profile(1)
        profile.profile_avatar.delete()

        set_image_on_imagefield(
            "test_set_avatar",
            imagefield=profile.profile_avatar
        )

        self.assertGreater(
            Profile.objects.get(pk=profile.pk).profile_avatar.size,
            1
        )
        profile.profile_avatar.delete()
