from message.models import InviteToOrganization
from model_bakery import baker


def make_invite_to_organization(
        number: int
) -> list[InviteToOrganization] | InviteToOrganization:
    invites = baker.make(
        'message.InviteToOrganization',
        _quantity=number,
    )
    if number == 1:
        return invites[0]
    return invites
