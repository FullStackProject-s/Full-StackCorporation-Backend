from general.tests.generic import BaseTestCaseGeneric
from general.utils.image_generator import generate_avatar


class TestImageGenerateAvatarUnit(BaseTestCaseGeneric):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_create_avatar_with_one_arg(self):
        avatar = generate_avatar('test')

        self.assertGreater(
            avatar.size,
            0
        )

    def test_create_avatar_with_many_arg(self):
        avatar = generate_avatar(*[
            f"{i}" for i in range(100)
        ])

        self.assertGreater(
            avatar.size,
            0
        )
