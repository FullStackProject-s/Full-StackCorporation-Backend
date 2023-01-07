from .user import create_users_list
from user.models.profile import Profile


def create_profiles(profile_numbers: int) -> list[Profile]:
    users = create_users_list(profile_numbers)

    return [
        Profile.objects.create(
            user=user,
            about_user=f'profile something {index}'
        ) for index, user in enumerate(users, start=1)
    ]
