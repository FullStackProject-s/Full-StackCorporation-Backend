from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from message.serializers import ReassignmentSerializer
from message.tests.utils import create_reassignment
from message.models import Reassignment

from project.tests.utils import create_projects, create_teams

from user.models import CustomUser
from user.tests.utils import create_users_list


class ReassignmentTestCase(APITestCase):
    """
    Test Cases for :model:`message.Reassignment`.
    """
    all_reassignment_url = reverse('all-reassignments')
    create_reassignment_url = reverse('create-reassignment')

    retrieve_reassignment = 'reassignment'
    delete_reassignment = 'delete-reassignment'
    update_reassignment = 'update-reassignment'

    reassignment_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, reassignment in enumerate(
                create_reassignment(cls.reassignment_count),
                start=1
        ):
            setattr(
                cls,
                f'reassignment_{index}',
                reassignment
            )
        _keyword = 'reassignment'

        cls.login_user = CustomUser.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_reassignments(self):
        response = self.client.get(self.all_reassignment_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.reassignment_count
        )

    def test_reassignment_retrieve(self):
        reassignment = self.reassignment_1
        pk = self.reassignment_1.pk
        response = self.client.get(
            reverse(self.retrieve_reassignment, kwargs={'pk': pk})
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_json['confirmed'],
            False
        )
        self.assertEqual(
            response_json['text'],
            reassignment.text
        )
        self.assertEqual(
            response_json,
            ReassignmentSerializer(reassignment).data
        )

    #
    def test_reassignment_create(self):
        name = 'test_reassignment_create'

        start = abs(hash(name))
        user = create_users_list(
            start,
            start=start,
            keyword=name
        )[0]

        proj_1, proj_2 = create_projects(
            start + 1,
            start=start,
            keyword=name
        )
        team_1, team_2 = create_teams(
            start + 1,
            start=start,
            keyword=name
        )
        json = {
            "creator": user.pk,
            "text": name,
            "from_project": proj_1.pk,
            "to_project": proj_2.pk,
            "from_team": team_1.pk,
            "to_team": team_2.pk

        }
        response = self.client.post(
            self.create_reassignment_url,
            data=json,
        )
        response_json = response.json()

        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response_json['confirmed'],
            False
        )
        self.assertEqual(
            Reassignment.objects.get(pk=pk).confirmed,
            False
        )

    #
    def test_delete_reassignment(self):
        pk = self.reassignment_1.pk

        response = self.client.delete(
            reverse(
                self.delete_reassignment,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Reassignment.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_reassignment(self):
        reassignment = self.reassignment_2
        pk = reassignment.pk
        name = 'test_put_reassignment'

        start = abs(hash(name))
        user = create_users_list(
            start,
            start=start,
            keyword=name
        )[0]

        proj_1, proj_2 = create_projects(
            start + 1,
            start=start,
            keyword=name
        )
        team_1, team_2 = create_teams(
            start + 1,
            start=start,
            keyword=name
        )
        json = {
            "creator": user.pk,
            "text": name,
            "from_project": proj_1.pk,
            "to_project": proj_2.pk,
            "from_team": team_1.pk,
            "to_team": team_2.pk,
            'confirmed': True

        }
        response = self.client.put(
            reverse(
                self.update_reassignment,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()

        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_json['confirmed'],
            True
        )
        self.assertEqual(
            Reassignment.objects.get(pk=pk).confirmed,
            True
        )

    def test_patch_reassignment(self):
        reassignment = self.reassignment_2
        pk = reassignment.pk
        name = 'test_patch_reassignment'

        json = {
            'text': name,
        }
        response = self.client.patch(
            reverse(
                self.update_reassignment,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Reassignment.objects.get(pk=pk).text,
            response_json['text']
        )
