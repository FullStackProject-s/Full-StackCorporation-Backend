from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric

from message.serializers import InviteToOrganizationSerializer
from message.models import InviteToOrganization
from message.models.consts import InviteStatus

from general.tests.model_factory import (
    make_user,
    make_invite_to_organization,
    make_organization
)


class BaseInviteToOrganizationTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`message.InviteToOrganization`.
    """
    all_objects_url = reverse('all-invites')
    create_object_url = reverse('create-invite')

    retrieve_object_url = 'invite'
    delete_object_url = 'delete-invite'
    update_object_url = 'update-invite'

    make_method = make_invite_to_organization
    serializer_class = InviteToOrganizationSerializer
    model_class = InviteToOrganization

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class InviteToOrganizationTestCase(BaseInviteToOrganizationTestCase):
    def test_get_all_invites(self):
        self._test_get_all_objects()

    def test_invite_retrieve(self):
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['status'],
            InviteStatus.WAITING
        )

    def test_invite_create(self):
        user = make_user(1)
        org = make_organization(1)
        json = {
            "creator": user.pk,
            'to_organization': org.pk,
            "text": 'test_invite_create',
        }
        response_json = self._test_create_object(json).json()

        pk = response_json['pk']

        self.assertEqual(
            response_json['status'],
            InviteToOrganization.objects.get(pk=pk).status
        )
        self.assertEqual(
            response_json['to_organization'],
            org.pk
        )

    def test_delete_invite(self):
        self._test_delete_object()

    def test_put_invite(self):
        self.default_object_number = 2

        json = {
            "text": 'test_put_invite',
            'status': InviteStatus.REJECTED
        }
        response_json = self._test_put_object(json).json()

        self.assertEqual(
            response_json['status'],
            json['status']
        )

    def test_patch_invite(self):
        self.default_object_number = 3

        json = {
            'status': InviteStatus.CONFIRMED
        }
        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            response_json['status'],
            InviteStatus.CONFIRMED
        )
