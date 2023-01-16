import os

CORS_ALLOWED_ORIGINS = [
    f"http://{os.getenv('CORS_ALLOWED')}",
]

CORS_ALLOW_CREDENTIALS = True
