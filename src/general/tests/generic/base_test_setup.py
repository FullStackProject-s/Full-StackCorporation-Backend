from typing import Callable

from rest_framework.test import APITestCase

from general.tests.model_factory import make_user


class BaseTestCaseSetupGeneric(APITestCase):
    """
    Base setup testCase.    
    """
    number_of_objects: int = 4
    make_method: Callable[[int], list] | None = None

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

    def setUp(self):
        self.client.force_login(self.base_login_user)
