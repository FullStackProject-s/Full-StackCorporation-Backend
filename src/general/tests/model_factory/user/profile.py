from user.models import Profile
from model_bakery import baker


def make_profile(number: int) -> list[Profile] | Profile:
    profiles = baker.make(
        'user.Profile',
        _quantity=number,
        is_active=True
    )
    if number == 1:
        return profiles[0]
    return profiles
