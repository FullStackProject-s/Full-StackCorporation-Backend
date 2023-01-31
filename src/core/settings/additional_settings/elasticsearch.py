import os

ELASTICSEARCH_DSL = {
    'default': {
        "hosts": os.getenv('ELASTICSEARCH').split()
    }
}
