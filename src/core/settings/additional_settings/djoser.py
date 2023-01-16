import os

DOMAIN = os.getenv('FRONT_DOMAIN')
SITE_NAME = os.getenv('SITE_NAME')
DJOSER = {
    # Password rest + reset url
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,

    # User activation + activation url
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,

    'SERIALIZERS': {
        'user_create': 'user.serializers.CustomUserSerializer',
        'user': 'user.serializers.CustomUserShowSerializer',
    }
}
