from django.urls import reverse

from general.tests.generic import BaseTestCaseGeneric

from message.serializers import ReassignmentSerializer
from message.models import Reassignment

from general.tests.model_factory import (
    make_user,
    make_project,
    make_team,
    make_reassignment,
    make_organization
)


class BaseReassignmentTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`message.Reassignment`.
    """
    all_objects_url = reverse('all-reassignments')
    create_object_url = reverse('create-reassignment')

    retrieve_object_url = 'reassignment'
    delete_object_url = 'delete-reassignment'
    update_object_url = 'update-reassignment'

    make_method = make_reassignment
    serializer_class = ReassignmentSerializer
    model_class = Reassignment

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class ReassignmentTestCase(BaseReassignmentTestCase):
    def test_get_all_reassignments(self):
        self._test_get_all_objects()

    def test_reassignment_retrieve(self):
        reassignment = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['confirmed'],
            False
        )
        self.assertEqual(
            response_json['text'],
            reassignment.text
        )

    def test_reassignment_create(self):
        user = make_user(1)
        org = make_organization(1)
        proj_1, proj_2 = make_project(2)
        team_1, team_2 = make_team(2)

        json = {
            "creator": user.pk,
            'organization': org.pk,
            "text": 'test_reassignment_create',
            "from_project": proj_1.pk,
            "to_project": proj_2.pk,
            "from_team": team_1.pk,
            "to_team": team_2.pk

        }
        response_json = self._test_create_object(json).json()

        pk = response_json['pk']

        self.assertEqual(
            response_json['confirmed'],
            False
        )
        self.assertEqual(
            Reassignment.objects.get(pk=pk).confirmed,
            False
        )

    def test_delete_reassignment(self):
        self._test_delete_object()

    def test_put_reassignment(self):
        pk = self.obj_2.pk
        self.default_object_number = 2

        user = make_user(1)
        proj_1, proj_2 = make_project(2)
        team_1, team_2 = make_team(2)

        json = {
            "creator": user.pk,
            "text": 'test_put_reassignment',
            "from_project": proj_1.pk,
            "to_project": proj_2.pk,
            "from_team": team_1.pk,
            "to_team": team_2.pk,
            'confirmed': True

        }
        response_json = self._test_put_object(json).json()

        self.assertEqual(
            response_json['confirmed'],
            True
        )
        self.assertEqual(
            Reassignment.objects.get(pk=pk).confirmed,
            True
        )

    def test_patch_reassignment(self):
        pk = self.obj_2.pk
        self.default_object_number = 2

        json = {
            'text': 'test_patch_reassignment',
        }
        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            Reassignment.objects.get(pk=pk).text,
            response_json['text']
        )
