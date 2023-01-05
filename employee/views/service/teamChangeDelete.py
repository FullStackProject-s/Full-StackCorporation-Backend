from general.services import PostResponse
from project.models import Team


class DeletePersonalTeamViewMixin:

    def _post_delete_team(self, message):
        dev = self.get_object()
        dev.team = None
        dev.save()
        return PostResponse.response_ok(message)


class ChangePersonalTeamViewMixin:
    def _post_change_team(
            self,
            message,
            team_name
    ):
        dev = self.get_object()

        if x := Team.objects.filter(team_name=team_name):
            dev.team = x.first()
            dev.save()
            return PostResponse.response_ok(message)
        return PostResponse.not_found_response('Team not found')
