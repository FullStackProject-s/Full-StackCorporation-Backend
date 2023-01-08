from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from employee.models import Developer, ProjectManager
from project.models import Team
from project.serializer import (
    TeamSerializer,
    TeamTeamLeadSerializer,
    TeamProjectManagerSerializer
)
from project.tests.utils import create_teams
from employee.tests.utils import create_developers, create_project_managers

from user.models import CustomUser


class DeveloperTestCase(APITestCase):
    """
    Test Cases for :model:`project.Team`.
    """
    all_teams_url = reverse('all-teams')
    create_team_url = reverse('create-team')

    retrieve_team = 'team'
    delete_team = 'delete-team'
    team_change_name = 'team-change-name'

    team_update_team_lead = 'team-update-team-lead'
    team_remove_team_lead = 'team-remove-team-lead'

    team_update_project_manager = 'team-update-project-manager'
    team_remove_project_manager = 'team-remove-project-manager'

    team_update_developers = 'team-update-developers'
    team_remove_developers = 'team-remove-developers'

    team_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, team in enumerate(
                create_teams(cls.team_count),
                start=1
        ):
            setattr(cls,
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
        json = {
            'team_name': "team_create_name"
        }
        response = self.client.post(
            self.create_team_url,
            data=json
        )

        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            json
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
                self.team_change_name,
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
            response_json,
            json
        )
        self.assertEqual(
            response_json['team_name'],
            Team.objects.get(pk=pk).team_name
        )

    def test_team_name_patch_team(self):
        json = {
            'team_name': 'put_team_name'
        }
        pk = self.team_3.pk
        response = self.client.patch(
            reverse(
                self.team_change_name,
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
            response_json,
            json
        )
        self.assertEqual(
            response_json['team_name'],
            Team.objects.get(pk=pk).team_name
        )

    def test_team_update_team_lead(self):
        team = self.team_2
        start = abs(hash('test_team_update_team_lead'))
        developer = create_developers(
            start,
            start=start
        )[0]
        json = {
            'team_lead': developer.profile.user.username
        }
        pk = team.pk
        response = self.client.post(
            reverse(
                self.team_update_team_lead,
                kwargs={'pk': pk}
            ),
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            team.team_name,
            Developer.objects.get(pk=developer.pk).team.team_name
        )
        self.assertNotEqual(
            TeamTeamLeadSerializer(Team.objects.get(pk=pk)).data,
            json
        )

    def test_team_remove_team_lead(self):
        start = abs(hash('test_team_remove_team_lead'))
        team = self.team_3
        developer = create_developers(
            start,
            start=start
        )[0]
        team.team_lead = developer
        team.save()

        developer.team = team
        developer.save()

        json = {
            'team_lead': developer.profile.user.username
        }
        pk = team.pk
        response = self.client.post(
            reverse(
                self.team_remove_team_lead,
                kwargs={'pk': pk}
            ),
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Team.objects.get(pk=team.pk).team_lead,
            None
        )
        self.assertEqual(
            Developer.objects.get(pk=developer.pk).team,
            None
        )

    def test_team_update_project_manager(self):
        team = self.team_2
        start = abs(hash('test_team_update_project_manager'))
        project_manager = create_project_managers(
            start,
            start=start
        )[0]
        json = {
            'project_manager': project_manager.profile.user.username
        }
        pk = team.pk
        response = self.client.post(
            reverse(
                self.team_update_project_manager,
                kwargs={'pk': pk}
            ),
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            team.team_name,
            ProjectManager.objects.get(pk=project_manager.pk).team.team_name
        )
        self.assertNotEqual(
            TeamProjectManagerSerializer(Team.objects.get(pk=pk)).data,
            json
        )

    def test_team_remove_project_manager(self):
        team = self.team_3
        start = abs(hash('test_team_remove_project_manager'))
        project_manager = create_project_managers(
            start,
            start=start
        )[0]
        team.project_manager = project_manager
        project_manager.team = team
        team.save()
        project_manager.save()

        json = {
            'project_manager': project_manager.profile.user.username
        }
        pk = team.pk
        response = self.client.post(
            reverse(
                self.team_remove_project_manager,
                kwargs={'pk': pk}
            ),
            data=json
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Team.objects.get(pk=team.pk).project_manager,
            None
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=project_manager.pk).team,
            None
        )

    def test_team_update_developers(self):
        team = self.team_4
        pk = team.pk
        start = abs(hash('test_team_update_developers'))
        developers = create_developers(
            start + self.team_count,
            start=start
        )
        developers_name_list = list(map(
            lambda x: x.profile.user.username,
            developers
        ))

        json = {
            'developers': developers_name_list
        }
        response = self.client.post(
            reverse(
                self.team_update_developers,
                kwargs={'pk': pk}
            ),
            data=json,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        all_team_devs = Team.objects.get(pk=team.pk).developers.all()

        for developer in developers:
            dev = Developer.objects.get(pk=developer.pk)

            self.assertEqual(
                dev.team,
                team
            )
            self.assertEqual(
                dev in all_team_devs,
                True
            )

    def test_team_remove_developers(self):
        team = self.team_4
        pk = team.pk
        start = abs(hash('test_team_remove_developers'))
        developers = create_developers(
            start + self.team_count,
            start=start
        )
        developers_name_list = list(map(
            lambda x: x.profile.user.username,
            developers
        ))

        json = {
            'developers': developers_name_list[0: self.team_count // 2]
        }
        response = self.client.post(
            reverse(
                self.team_remove_developers,
                kwargs={'pk': pk}
            ),
            data=json,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        all_team_devs = Team.objects.get(pk=team.pk).developers.all()

        for developer in developers:
            dev = Developer.objects.get(pk=developer.pk)

            self.assertEqual(
                dev.team,
                None
            )
            self.assertEqual(
                dev not in all_team_devs,
                True
            )
