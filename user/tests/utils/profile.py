from .user import create_users_list
from user.models.profile import Profile


def create_profiles(profile_numbers: int, start=1) -> list[Profile]:
    create_users_list(profile_numbers, start=start)

    for index, profile in enumerate(
            Profile.objects.all(),
            start=start
    ):
        profile.about_user = f'profile something {index}'
        profile.save()
    return Profile.objects.all()
