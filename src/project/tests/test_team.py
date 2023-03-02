from django.urls import reverse

from rest_framework import status

from employee.models import Developer, ProjectManager

from general.tests.generic import BaseTestCaseGeneric
from general.tests.model_factory import (
    make_team,
    make_developer,
    make_project_manager,
    make_project

)

from project.models import Team, Project
from project.serializer import TeamSerializer


class BaseTeamTestCase(BaseTestCaseGeneric):
    """
    Test Cases for :model:`project.Team`.
    """
    all_objects_url = reverse('all-teams')
    create_object_url = reverse('create-team')

    retrieve_object_url = 'team'
    delete_object_url = 'delete-team'
    update_object_url = 'update-team'

    make_method = make_team
    serializer_class = TeamSerializer
    model_class = Team

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()


class TeamTestCase(BaseTeamTestCase):
    def test_get_all_teams(self):
        self._test_get_all_objects()

    def test_team_retrieve(self):
        team = self.obj_1
        response_json = self._test_retrieve_object().json()

        self.assertEqual(
            response_json['team_lead'],
            team.team_lead
        )
        self.assertEqual(
            response_json['project_manager'],
            team.project_manager
        )

    def test_team_create(self):
        proj_manager = make_project_manager(1)
        team_lead, dev_1, dev_2 = make_developer(3)
        proj = make_project(1)
        self._add_to_organization(
            proj.organization,
            team_lead,
            dev_1,
            dev_2,
            proj_manager
        )
        json = {
            'team_name': "team_create_name",
            'team_lead': team_lead.pk,
            'project': proj.pk,
            'project_manager': proj_manager.pk,
            'developers': [
                dev_1.pk,
                dev_2.pk
            ]

        }
        response = self.client.post(
            self.create_object_url,
            data=json
        )
        response_json = response.json()

        team = Team.objects.get(pk=response_json['pk'])

        self.assertIn(
            team,
            Project.objects.get(pk=proj.pk).teams.all()
        )
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
        self._test_delete_object()

    def test_team_name_put_team(self):
        proj = make_project(1)
        json = {
            'project': proj.pk,
            'team_name': 'put_team_name'
        }
        response_json = self._test_put_object(json).json()
        self.assertEqual(
            response_json['team_name'],
            Team.objects.get(pk=self.obj_1.pk).team_name
        )

    def test_team_lead_patch_team(self):
        team = self.obj_1
        dev_1, dev_2 = make_developer(2)

        self._add_to_organization(
            team.project.organization,
            dev_1,
            dev_2
        )

        json = {
            'team_name': 'test_team_lead_patch_team',
            'team_lead': dev_1.pk
        }

        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            Team.objects.get(pk=response_json['pk']).team_lead,
            dev_1
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_1.pk).team,
            team
        )

        # Set's second's team lead
        json = {
            'team_lead': dev_2.pk
        }

        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            Team.objects.get(pk=response_json['pk']).team_lead,
            dev_2
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_2.pk).team,
            team
        )
        self.assertEqual(
            Developer.objects.get(pk=dev_1.pk).team,
            None
        )

    def test_project_manager_patch_team(self):
        team = self.obj_1
        project_manager_1, project_manager_2 = make_project_manager(2)

        self._add_to_organization(
            team.project.organization,
            project_manager_1,
            project_manager_2
        )

        json = {
            'team_name': 'test_project_manager_patch_team',
            'project_manager': project_manager_1.pk
        }

        response_json = self._test_patch_object(json).json()

        self.assertEqual(
            Team.objects.get(pk=response_json['pk']).project_manager,
            project_manager_1
        )
        self.assertEqual(
            ProjectManager.objects.get(pk=project_manager_1.pk).team,
            team
        )

        # Set's second's project manager
        json = {
            'project_manager': project_manager_2.pk
        }

        response_json = self._test_patch_object(json).json()

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
        team = self.obj_2
        self.default_object_number = 2

        dev_1, dev_2, dev_3, dev_4 = make_developer(4)
        self._add_to_organization(
            team.project.organization,
            dev_1,
            dev_2,
            dev_3,
            dev_4
        )

        pk = team.pk

        json = {
            'team_name': 'test_developers_patch_team',
            'developers': [
                dev_1.pk,
                dev_2.pk
            ]
        }
        self._test_patch_object(json).json()

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

        # Set's second's developers set
        json = {
            'developers': [
                dev_3.pk,
                dev_4.pk
            ]
        }
        self._test_patch_object(json).json()

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

    def test_random_employee_add_test(self):
        developer = make_developer(1)
        json = {
            'developers': [
                developer.pk
            ]
        }

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': self.obj_1.pk}),
            data=json
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def _add_to_organization(self, organization, *employees):
        organization.members.add(
            *list(map(lambda employee: employee.profile.user, employees))
        )
        organization.save()
