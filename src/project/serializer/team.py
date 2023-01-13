from employee.models import Developer, ProjectManager
from employee.serializers import (
    DeveloperShowSerializer,
    ProjectManagerShowSerializer
)

from project.serializer.services import _update_personal
from project.serializer.generics import BaseTeamSerializer


class TeamShowSerializer(BaseTeamSerializer):
    team_lead = DeveloperShowSerializer()
    project_manager = ProjectManagerShowSerializer()
    developers = DeveloperShowSerializer(many=True)


class TeamSerializer(BaseTeamSerializer):
    def to_representation(self, instance):
        return TeamShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)
        if team_lead_ := instance.team_lead:
            team_lead = Developer.objects.get(pk=team_lead_.pk)
            team_lead.team = instance
            team_lead.save()
        if project_manger_ := instance.project_manager:
            project_manger = ProjectManager.objects.get(pk=project_manger_.pk)
            project_manger.team = instance
            project_manger.save()
        if developers := instance.developers.all():
            for developer in developers:
                developer.set_team(instance)
        return instance

    def update(self, instance, validated_data):
        _update_personal(instance, validated_data)
        return super().update(instance, validated_data)
