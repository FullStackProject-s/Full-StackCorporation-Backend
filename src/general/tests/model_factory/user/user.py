from django.contrib.auth import get_user_model
from model_bakery import baker

User = get_user_model()


def make_user(number: int) -> list[User] | User:
    users = baker.make(
        'user.CustomUser',
        _quantity=number,
        is_active=True,
    )
    if number == 1:
        return users[0]
    return users
