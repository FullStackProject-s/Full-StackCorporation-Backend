from rest_framework import status
from rest_framework.response import Response


class PostResponse:
    @staticmethod
    def not_found_response(message_text):
        return Response(
            {
                "error": message_text
            },
            status=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def response_ok(message_text):
        return Response(
            {"message": message_text},
            status=status.HTTP_200_OK
        )
