from .user import create_users_list
from user.models.profile import Profile


def create_profiles(profile_numbers: int, start=1) -> list[Profile]:
    users = create_users_list(profile_numbers, start=start)

    return [
        Profile.objects.create(
            user=user,
            about_user=f'profile something {index}'
        ) for index, user in enumerate(users, start=start)
    ]
