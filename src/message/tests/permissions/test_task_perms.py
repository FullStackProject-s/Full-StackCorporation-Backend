from rest_framework import status
from rest_framework.reverse import reverse

from general.tests.generic import BaseTestCasePermissionsGeneric
from general.tests.model_factory import (
    make_user,
    make_administrator,
    make_organization, make_task
)
from message.tests.test_task import (
    BaseTaskTestCase,
)


class TaskPermissionsTestCase(
    BaseTaskTestCase,
    BaseTestCasePermissionsGeneric
):
    """
    Test Cases for IsAdministratorOrOwnerOrReadOnlyInvite permission.
    """

    def test_get_all_tasks_perms(self):
        self._test_get_all_objects()

    def test_task_retrieve_perms(self):
        self._test_retrieve_object()

    def test_delete_task_perms(self):
        self._test_delete_object_perms()

    def test_put_task_perms(self):
        self._test_put_object_perms()

    def test_patch_task_perms(self):
        self._test_patch_object_perms()

    def test_task_create_user_perms(self):
        user = make_user(1)
        org = make_organization(1)

        self.client.force_login(user)
        self._set_credentials_for_user(user)

        json = {
            'creator': user.pk,
            'text': 'test_task_create_user_perms',
            'organization': org.pk
        }
        response = self.client.post(
            self.create_object_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_create_task_perms(self):
        org = make_organization(1)

        admin = make_administrator(1)
        admin_user = admin.profile.user
        admin_user.is_active = True
        admin_user.save()

        owner = make_user(1)

        org.owner = owner
        org.members.add(admin_user)
        org.save()

        json = {
            'creator': owner.pk,
            'text': 'test_create_task_perms',
            'organization': org.pk
        }

        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        response = self.client.post(
            self.create_object_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        json['creator'] = admin_user.pk
        self.client.force_login(admin_user)
        self._set_credentials_for_user(admin_user)

        response = self.client.post(
            self.create_object_url,
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_patch_task_owner_admin_perms(self):
        task = make_task(1)

        org = make_organization(1)

        admin = make_administrator(1)
        admin_user = admin.profile.user
        admin_user.is_active = True
        admin_user.save()

        owner = make_user(1)

        org.owner = owner
        org.members.add(admin_user)
        org.save()

        task.organization = org
        task.save()

        self.client.force_login(owner)
        self._set_credentials_for_user(owner)

        url = reverse(self.update_object_url, kwargs={'pk': task.pk})
        response = self.client.patch(
            url,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.client.force_login(admin_user)
        self._set_credentials_for_user(admin_user)

        response = self.client.patch(
            url,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
