from employee.views.service.developer_post import DeveloperPostResponse
from project.models import Team


class DeletePersonalTeamViewMixin:

    def _post_delete_team(self, message):
        dev = self.get_object()
        dev.team = None
        dev.save()
        return DeveloperPostResponse.response_ok({
            "message": message
        })


class ChangePersonalTeamViewMixin:
    def _post_change_team(self, request, message):
        dev = self.get_object()

        if x := Team.objects.filter(team_name=request.data['team']):
            dev.team = x.first()
            dev.save()
            return DeveloperPostResponse.response_ok({
                "message": message
            })
        return DeveloperPostResponse.not_found_response('Team not found')
