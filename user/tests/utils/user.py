from django.contrib.auth import get_user_model

User = get_user_model()


def create_users_list(user_numbers: int, start=1) -> list[User]:
    return [
        User.objects.create_user(
            username=f'user_{i}',
            email=f'user{i}@example.com',
            password=f'user_{i}',
            first_name=f'first_{i}',
            last_name=f'last_{i}',
        ) for i in range(start, user_numbers + 1)
    ]
