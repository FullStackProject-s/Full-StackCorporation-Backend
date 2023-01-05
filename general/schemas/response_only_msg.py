from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema
)


def response_only_message(view_method_name):
    return extend_schema(
        examples=[
            OpenApiExample(
                'Valid example 1',
                value={
                    'Message': 'string',
                },
                request_only=False,
                response_only=True,
            ),
        ],
        request=None

    )(view_method_name)