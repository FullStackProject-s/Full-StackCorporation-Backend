from project.views.mixins import (
    TeamRemoveMainPersonalViewMixin,
    TeamUpdateMainPersonalViewMixin
)


class TeamBaseGenericRemoveUpdateMainPersonal:
    personal_model = None
    personal_relation_name = None


class TeamGenericRemovePersonal(
    TeamBaseGenericRemoveUpdateMainPersonal,
    TeamRemoveMainPersonalViewMixin
):
    pass


class TeamGenericUpdatePersonal(
    TeamBaseGenericRemoveUpdateMainPersonal,
    TeamUpdateMainPersonalViewMixin
):
    pass
