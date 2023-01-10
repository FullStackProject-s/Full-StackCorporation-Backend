from typing import Callable
from rest_framework import serializers

from employee.models import Developer
from general.services import response_many_to_many_api_views


class TeamRemoveUpdateDeveloper:
    def _change_developers(
            self,
            team,
            request,
            message: str,
            team_method: Callable[[Developer], None],
            developer_team
    ):
        developer_list = []
        developers_names = self._validate_request(request).data['developers']

        for developer_name in developers_names:
            if developer := Developer.objects.filter(
                    profile__user__username=developer_name
            ).first():
                if developer.team and developer.team != team:
                    raise serializers.ValidationError(
                        "Developer stated in different Team"
                    )
                if developer.team == team and developer_team is not None:
                    raise serializers.ValidationError(
                        "Developer already stated in this Team"
                    )
                team_method(developer)
                developer_list.append(developer)
                developer.team = developer_team

                team.save()
                developer.save()
        return response_many_to_many_api_views(
            developer_list,
            message,
            'Developers not found'
        )
