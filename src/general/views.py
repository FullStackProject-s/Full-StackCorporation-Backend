import random

import os

from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from employee.models import ProjectManager, Developer
from general.models.utils import set_image_on_imagefield
from user.models import Profile
from project.models import Team, Project
from general.tests.model_factory import *
from .about import ABOUT

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


class CreateDeveloperUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if not User.objects.filter(
                username=os.getenv('USERNAME_FRONT')).exists():
            frontend_user = User.objects.create_user(
                username=os.getenv('USERNAME_FRONT'),
                password=os.getenv('PASSWORD_FRONT'),
                email=os.getenv('EMAIL_FRONT'),
                first_name=os.getenv('FIRST_NAME_FRONT'),
                last_name=os.getenv('SECOND_NAME_FRONT')
            )
            frontend_user.is_active = True
            frontend_user.save()

        if not Profile.objects.filter(
                user__username=os.getenv('USERNAME_FRONT')).exists():
            Profile.objects.create(
                user=User.objects.get(username=os.getenv('USERNAME_FRONT')),
                about_user=ABOUT
            )
        return Response()


class CreateFillDataView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        spec = make_specialty(40)
        developers = Developer.objects.all()
        admins = make_administrator(10)
        project_managers = make_project_manager(10)

        projects = make_project(50)
        owners = make_user(10)
        organization_ = make_organization(10)
        teams = make_team(10)

        # completed_tasks = make_completed_tasks(10)
        # reassignments = make_reassignment(10)
        # task = make_task(10)

        for profile in Profile.objects.all():
            set_image_on_imagefield(
                profile.user.username,
                profile.user.email,
                imagefield=profile.profile_avatar,
            )
        for index, (org, owner) in enumerate(zip(organization_, owners)):
            org.owner = owner
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

        for project in Project.objects.all():
            for team in Team.objects.all():
                project.teams.add(team)
            project.organization = organization_[random.randint(0, 9)]
            project.save()

        for index, (team_, project_manager_) in enumerate(
                zip(teams, ProjectManager.objects.all())
        ):
            team_ = Team.objects.get(pk=team_.pk)
            team_.team_lead = Developer.objects.get(pk=developers[index].pk)
            team_.save()
            for dev in Developer.objects.all():
                team_.developers.add(dev)
                team_.save()
            team_.project_manager = project_manager_
            team_.save()
        for dev in developers:
            dev.specialties.add(*spec)
            dev.save()
        return Response()
