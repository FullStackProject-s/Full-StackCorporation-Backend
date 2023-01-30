import os

CORS_ALLOWED_ORIGINS = [
    f'http://{domain}'
    for domain in os.getenv('CORS_ALLOWED').split()
]

CORS_ALLOW_CREDENTIALS = True
