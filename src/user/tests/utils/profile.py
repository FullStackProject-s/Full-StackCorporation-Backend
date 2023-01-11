from .user import create_users_list
from user.models.profile import Profile


def create_profiles(profile_numbers: int, start=1) -> list[Profile]:
    users = create_users_list(profile_numbers, start=start)
    profiles = []
    for index, user in enumerate(
            users,
            start=start
    ):
        profile = Profile.objects.get(user=user)
        profile.about_user = f'profile something {index}'
        profile.save()
        profiles.append(profile)
    return profiles
