from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from general.tests.generic import BaseTestCaseGeneric

User = get_user_model()


class CookieJWTTestCase(BaseTestCaseGeneric):
    token_delete_url = reverse('token-delete')
    token_refresh_url = reverse('token-refresh')
    token_obtain_tokens_url = reverse('token-obtain-pair')

    @classmethod
    def setUpTestData(cls):
        cls.base_login_user = User.objects.create_user(
            **{
                "username": "string",
                "email": "user@example.com",
                "first_name": "string",
                "last_name": "string",
                "password": "string"
            }
        )
        cls.base_login_user.is_active = True
        cls.base_login_user.save()

    def setUp(self):
        self.client.force_login(self.base_login_user)

    def test_cookie_tokens_obtain(self):
        response = self._get_token_obtain_response()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertIn(
            settings.COOKIE_REFRESH_TOKEN_NAME,
            response.cookies
        )
        self.assertIn(
            'access',
            response.json()
        )

    def test_cookie_token_refresh(self):
        self._get_token_obtain_response()

        response = self.client.post(self.token_refresh_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertIn(
            'access',
            response.json()
        )

    def test_cookie_token_delete(self):
        self._get_token_obtain_response()

        response_delete = self.client.post(self.token_delete_url)

        self.assertEqual(
            response_delete.status_code,
            status.HTTP_204_NO_CONTENT
        )

        response_refresh = self.client.post(self.token_refresh_url)

        self.assertEqual(
            response_refresh.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        response_again_delete = self.client.post(self.token_delete_url)

        self.assertEqual(
            response_again_delete.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def _get_token_obtain_response(self):
        json = {
            'username': 'string',
            'password': 'string'
        }
        response = self.client.post(
            self.token_obtain_tokens_url,
            data=json
        )
        return response
