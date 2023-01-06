from general import PostResponse


class TeamRemoveMainPersonalViewMixin:

    def _remove_personal(self, request, message):
        team = self.get_object()

        personal_name = self._validate_request(request).data[
            self.personal_relation_name
        ]

        if personal := self.personal_model.objects.filter(
                profile__user__username=personal_name
        ).first():
            setattr(personal, 'team', None)
            personal.save()

            setattr(team, self.personal_relation_name, None)
            team.save()

            return PostResponse.response_ok(message)
        return PostResponse.not_found_response("Personal not found")


class TeamUpdateMainPersonalViewMixin:

    def _update_personal(self, request, message):
        team = self.get_object()

        personal_name = self._validate_request(request).data[
            self.personal_relation_name
        ]
        if personal := self.personal_model.objects.filter(
                profile__user__username=personal_name
        ).first():
            setattr(team, self.personal_relation_name, personal)
            setattr(personal, 'team', team)

            personal.save()
            team.save()
            return PostResponse.response_ok(message)
        return PostResponse.not_found_response('Not found project manager')
