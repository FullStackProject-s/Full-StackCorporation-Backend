import logging

from typing import Callable

from django.contrib.auth import get_user_model
from django.test import override_settings

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.test import APITestCase

from general.tests.model_factory import make_user

User = get_user_model()

logging.disable(logging.CRITICAL)


@override_settings(TESTS_LAUNCHED=True)
class BaseTestCaseSetupGeneric(APITestCase):
    """
    Base setup testCase.    
    """

    number_of_objects: int = 4
    # function for create model objects
    make_method: Callable[[int], list] | None = None

    # tested serializer
    serializer_class = None
    # tested model
    model_class = None
    # default picked object number, obj_1
    default_object_number = 1

    base_login_user = None

    @classmethod
    def setUpTestData(cls):

        if cls.number_of_objects and cls.make_method:
            for index, obj in enumerate(
                    cls.make_method(cls.number_of_objects),
                    start=1
            ):
                setattr(
                    cls,
                    f'obj_{index}',
                    obj
                )

        # for only CustomUserTestCase
        if cls.make_method != make_user:
            cls.base_login_user = make_user(1)
        else:
            cls.base_login_user = cls.obj_1
        cls.refresh = RefreshToken.for_user(cls.base_login_user)
        cls.base_login_user.is_superuser = True
        cls.base_login_user.save()

    def setUp(self):
        self.client.force_login(self.base_login_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}'
        )
        self.default_object_number = 1

    def _set_credentials_for_user(self, user: User):
        refresh = RefreshToken.for_user(user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
        )


class BaseTestCaseSetupPermissionsGeneric(BaseTestCaseSetupGeneric):
    # default picked object to change -- obj_2
    default_changed_object_number = 2

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.base_login_user.is_superuser = False
        cls.base_login_user.save()
