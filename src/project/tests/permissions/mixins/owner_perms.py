from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from general.tests.model_factory import make_user
from organization.models import Organization

User = get_user_model()


class TestOwnerPermsMixin:
    def _test_object_owner_perms(self, object_, pk):
        owner = make_user(1)

        owner.is_active = True
        owner.save()

        org = Organization.objects.get(pk=pk)
        org.owner = owner
        org.save()

        self._run_patch_request_for_object(
            owner,
            object_
        )

    def _run_patch_request_for_object(self, owner: User, object_):
        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        response = self.client.patch(
            reverse(
                self.update_object_url,
                kwargs={'pk': object_.pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
