from django.urls import reverse

from rest_framework import status

from employee.models import Developer, ProjectManager
from employee.tests.utils import create_developers, create_project_managers
from general.tests import BaseTestCaseGeneric

from project.models import Team
from project.serializer import TeamSerializer

from project.tests.utils import create_teams

from user.models import CustomUser


class DeveloperTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`project.Team`.
    """
    all_teams_url = reverse('all-teams')
    create_team_url = reverse('create-team')

    retrieve_team = 'team'
    delete_team = 'delete-team'
    update_team = 'update-team'

    team_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, team in enumerate(
                create_teams(cls.team_count),
                start=1
        ):
            setattr(
                cls,
                f'team_{index}',
                team
            )
        _keyword = 'team'

        cls.login_user = CustomUser.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_teams(self):
        response = self.client.get(self.all_teams_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.team_count
        )

    def test_team_retrieve(self):
        team = self.team_2
        pk = self.team_2.pk
        response = self.client.get(
            reverse(self.retrieve_team, kwargs={'pk': pk})
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_json['team_lead'],
            team.team_lead
        )
        self.assertEqual(
            response_json['project_manager'],
            team.project_manager
        )
        self.assertEqual(
            response_json,
            TeamSerializer(team).data
        )

    def test_team_create(self):
        start_dev = abs(hash('test_team_create_dev'))
        start_proj = abs(hash('test_team_create_proj_manager'))
        proj_manager = create_project_managers(start_proj, start=start_proj)[0]
        team_lead, dev_1, dev_2 = create_developers(
            start_dev + 2,
            start=start_dev
        )
        json = {
            'team_name': "team_create_name",
            'team_lead': team_lead.pk,
            'project_manager': proj_manager.pk,
            'developers': [
                dev_1.pk,
                dev_2.pk
            ]

        }
        response = self.client.post(
            self.create_team_url,
            data=json,
            format='json'
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        team = Team.objects.get(pk=response_json['pk'])
        self.assertEqual(
            Developer.objects.get(pk=team_lead.pk).team.pk,
            team.pk
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=proj_manager.pk).team.pk,
            team.pk
        )
        self.assertEqual(
            list(team.developers.all()),
            [
                Developer.objects.get(pk=dev_1.pk),
                Developer.objects.get(pk=dev_2.pk)
            ]
        )

    def test_delete_team(self):
        pk = self.team_1.pk

        response = self.client.delete(
            reverse(
                self.delete_team,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Team.objects.filter(pk=pk).exists(),
            False
        )

    def test_team_name_put_team(self):
        json = {
            'team_name': 'put_team_name'
        }
        pk = self.team_4.pk
        response = self.client.put(
            reverse(
                self.update_team,
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
            response_json['team_name'],
            Team.objects.get(pk=pk).team_name
        )

    def test_team_lead_patch_team(self):
        name = 'test_team_lead_patch_team'
        team = self.team_3
        start = abs(hash(name))

        team_lead_1, team_lead_2 = create_developers(start + 1, start=start)

        pk = team.pk
        json = {
            'team_name': name,
            'team_lead': team_lead_1.pk
        }
        response = self.client.patch(
            reverse(
                self.update_team,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()

        # Set's first team_lead
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Team.objects.get(pk=response_json['pk']).team_lead,
            team_lead_1
        )
        self.assertEqual(
            Developer.objects.get(pk=team_lead_1.pk).team,
            team
        )

        # Set's second's team_lead
        json = {
            'team_lead': team_lead_2.pk
        }
        response = self.client.patch(
            reverse(
                self.update_team,
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
            Team.objects.get(pk=response_json['pk']).team_lead,
            team_lead_2
        )
        self.assertEqual(
            Developer.objects.get(pk=team_lead_2.pk).team,
            team
        )
        self.assertEqual(
            Developer.objects.get(pk=team_lead_1.pk).team,
            None
        )

    def test_project_manager_patch_team(self):
        name = 'test_project_manager_patch_team'
        team = self.team_3
        start = abs(hash(name))

        project_manager_1, project_manager_2 = create_project_managers(
            start + 1,
            start=start
        )

        pk = team.pk
        json = {
            'team_name': name,
            'project_manager': project_manager_1.pk
        }
        response = self.client.patch(
            reverse(
                self.update_team,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()

        # Set's first team_lead
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Team.objects.get(pk=response_json['pk']).project_manager,
            project_manager_1
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=project_manager_1.pk).team,
            team
        )

        # Set's second's team_lead
        json = {
            'project_manager': project_manager_2.pk
        }
        response = self.client.patch(
            reverse(
                self.update_team,
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
            Team.objects.get(pk=response_json['pk']).project_manager,
            project_manager_2
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=project_manager_2.pk).team,
            team
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=project_manager_1.pk).team,
            None
        )

    def test_developers_patch_team(self):
        name = 'test_developers_patch_team'
        team = self.team_3
        start = abs(hash(name))

        dev_1, dev_2, dev_3, dev_4 = create_developers(
            start + 3,
            start=start
        )

        pk = team.pk
        json = {
            'team_name': name,
            'developers': [
                dev_1.pk,
                dev_2.pk
            ]
        }
        response = self.client.patch(
            reverse(
                self.update_team,
                kwargs={'pk': pk}
            ),
            data=json,
            format='json'
        )
        response_json = response.json()
        pk = response_json['pk']

        # Set's first team_lead
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            list(Team.objects.get(pk=pk).developers.all()),
            [dev_1, dev_2]
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_1.pk).team,
            team
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_2.pk).team,
            team
        )

        # Set's second's team_lead
        json = {
            'developers': [
                dev_3.pk,
                dev_4.pk
            ]
        }
        response = self.client.patch(
            reverse(
                self.update_team,
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
            list(Team.objects.get(pk=pk).developers.all()),
            [dev_3, dev_4]
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_3.pk).team,
            team
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_4.pk).team,
            team
        )

        self.assertEqual(
            Developer.objects.get(pk=dev_1.pk).team,
            None
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_2.pk).team,
            None
        )
