from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CheckUserContainsInOrganizationMixin:
    def _validate_user_members(self, attrs):
        self.instance_super = attrs.get('project', None) or \
                              self.instance.project

        if team_lead := attrs.get('team_lead', None):
            self.check_user_contains_in_organization(team_lead)
        if project_manager := attrs.get('project_manager', None):
            self.check_user_contains_in_organization(project_manager)
        if developers := attrs.get('developers', None):
            self.check_user_contains_in_organization(*developers)
        return attrs

    def check_user_contains_in_organization(self, *employees):
        for employee in employees:
            user = employee.profile.user
            if user not in self.instance_super.organization.members.all():
                raise serializers.ValidationError(
                    'User: %s not in organization ' % user.username
                )
