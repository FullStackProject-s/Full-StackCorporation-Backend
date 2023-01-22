from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema
)


def image_upload_schema(serializer, description):
    return extend_schema(responses={
        202: OpenApiResponse(
            response=serializer,
            description=description
        )
    })
