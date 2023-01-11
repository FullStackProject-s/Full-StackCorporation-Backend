from django.contrib.auth import get_user_model

User = get_user_model()


def create_users_list(
        user_numbers: int,
        start=1,
        keyword=''
) -> list[User]:
    keyword = 'create_users_list' + keyword
    return [
        User.objects.create_user(
            username=f'user_{i}{keyword}',
            email=f'user{i}@example.com{keyword}',
            password=f'user_{i}{keyword}',
            first_name=f'first_{i}{keyword}',
            last_name=f'last_{i}{keyword}',
        ) for i in range(start, user_numbers + 1)
    ]
