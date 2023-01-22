from rest_framework import status


class TestMeEndpointMixin:
    def _test_me(self, make_method):
        reqeust = lambda: self.client.get(self.obj_self_url)  # noqa
        response = reqeust()
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        employee = make_method(1)
        user = employee.profile.user
        user.is_active = True
        user.save()

        self.client.force_login(user)
        self._set_credentials_for_user(user)
        response = reqeust()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            self.serializer_class(employee).data
        )
