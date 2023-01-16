import os

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
BROKER_URL = f'redis://{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}'
CELERY_RESULT_BACKEND = f'redis://{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}'
