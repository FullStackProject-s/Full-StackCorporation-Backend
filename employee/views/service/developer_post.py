from rest_framework import status
from rest_framework.response import Response


class DeveloperPostResponse:
    @staticmethod
    def not_found_response(message_text):
        return Response(
            {
                "error": message_text
            },
            status=status.HTTP_404_NOT_FOUND
        )

    @staticmethod
    def response_ok(message_dict):
        return Response(
            message_dict,
            status=status.HTTP_404_NOT_FOUND
        )
