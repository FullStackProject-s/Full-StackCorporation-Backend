from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from general.models.utils import set_image_on_imagefield
from user.models import Profile
from general.tests.model_factory import *

"""
ONLY FOR DEVELOPMENT
"""
User = get_user_model()


class CreateSuperUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if not User.objects.filter(username='bol4onok').exists():
            User.objects.create_superuser(
                username='bol4onok',
                password='bol4onok',
                email='email@mail.com',
                first_name='1',
                last_name='2'
            )
        return Response()


class CreateFillDataView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        developers = make_developer(40)
        admins = make_administrator(10)
        project_managers = make_project_manager(10)

        projects = make_project(50)
        organization_ = make_organization(10)

        teams = make_team(10)

        completed_tasks = make_completed_tasks(10)
        reassignments = make_reassignment(10)
        task = make_task(10)

        for profile in Profile.objects.all():
            set_image_on_imagefield(
                profile.user.username,
                profile.user.email,
                imagefield=profile.profile_avatar,
            )
        for index, org in enumerate(organization_):
            for proj in projects:
                org.projects.add(proj)
            for dev in developers:
                org.members.add(dev.profile.user)
            for proj in project_managers:
                org.members.add(proj.profile.user)

            org.members.add(admins[index].profile.user)
            set_image_on_imagefield(
                org.organization_name,
                imagefield=org.organization_avatar,
            )
            org.save()

        for project in projects:
            for team in teams:
                project.teams.add(team)
            project.save()

        for index, team in enumerate(teams):
            team.team_lead = developers[index]
            for dev in developers:
                team.developers.add(dev)
            for proj in project_managers:
                team.project_manager = proj
            team.save()

        return Response()
