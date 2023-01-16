import os

DOMAIN = os.getenv('FRONT_DOMAIN')
SITE_NAME = os.getenv('SITE_NAME')
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
}
