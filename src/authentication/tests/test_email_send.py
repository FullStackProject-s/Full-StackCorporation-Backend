from django.core import mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

from rest_framework import status

from djoser import utils

from core.celery import app

from general.tests.generic.base_test_setup import BaseTestCaseSetupGeneric
from general.tests.model_factory import make_user

from user.models.consts import StaffRole

User = get_user_model()


class CeleryDjoserEmailTestCase(BaseTestCaseSetupGeneric):
    """
    Tests for overriding djoser viewset endpoints.
    """
    create_user_url = reverse('customuser-list')
    activate_user_url = reverse('customuser-activation')
    reset_password_url = reverse('customuser-reset-password')
    reset_password_activate_url = reverse('customuser-reset-password-confirm')

    @classmethod
    def setUpTestData(cls):
        app.conf.task_always_eager = True

    def setUp(self):
        pass

    def test_create_user(self):
        """
        Test POST creating user endpoint.
        """

        json = {
            "username": "string",
            "email": "user@example.com",
            "first_name": "string",
            "last_name": "string",
            'staff_role': StaffRole.DEVELOPER,
            "password": "string"
        }
        response = self.client.post(
            self.create_user_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f'Account activation on {settings.SITE_NAME}'
        )

    def test_activate_user(self):
        """
        Test POST activate user endpoint.
        """

        user = make_user(1)
        user.is_active = False
        user.save()

        json = {
            'uid': utils.encode_uid(user.pk),
            'token': default_token_generator.make_token(user)
        }
        response = self.client.post(
            self.activate_user_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f'{settings.SITE_NAME} - '
            'Your account has been successfully created and activated!'
        )
        self.assertEqual(
            User.objects.get(pk=user.pk).is_active,
            True
        )

    def test_reset_password_user(self):
        """
        Test POST reset password user endpoint.
        """

        user = make_user(1)
        user.is_active = True
        user.save()

        json = {
            'email': user.email,
        }
        response = self.client.post(
            self.reset_password_url,
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f'Password reset on {settings.SITE_NAME}'
        )

    def test_reset_password_confirmation_user(self):
        """
        Test POST reset password confirmation user endpoint.
        """

        user = make_user(1)
        user.is_active = True
        user.save()

        json = {
            'uid': utils.encode_uid(user.pk),
            'token': default_token_generator.make_token(user),
            'new_password': user.password
        }

        response = self.client.post(
            self.reset_password_activate_url,
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f'{settings.SITE_NAME} - '
            f'Your password has been successfully changed!'
        )
