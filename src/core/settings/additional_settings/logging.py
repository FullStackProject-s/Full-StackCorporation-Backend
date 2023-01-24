LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "formatters": {
            "rich": {
                "datefmt": "[%X]"
            }
        },
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-4s %(message)s'
        }
    },
    'handlers': {
        'django-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '../logs/django-logs.log'
        },
        'auth': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '../logs/apps/auth-logs.log'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'rich.logging.RichHandler',
            'formatter': 'console'
        },
    },
    'loggers': {
        'authentication': {
            'handlers': ['auth', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django': {
            'handlers': ['django-file', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['django-file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
