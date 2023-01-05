from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema
)


def response_true_message(view_method_name):
    return extend_schema(
        examples=[
            OpenApiExample(
                'Valid example 1',
                value={
                    'Message': 'string',
                },
                response_only=True
            ),
        ],
    )(view_method_name)


def response_true_request_false_message(view_method_name):
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
