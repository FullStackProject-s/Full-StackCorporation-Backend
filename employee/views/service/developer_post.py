from rest_framework import status
from rest_framework.response import Response


class DeveloperPostNotFound:
    @staticmethod
    def not_found_response(message_text):
        return Response(
            {
                "error": message_text
            },
            status=status.HTTP_404_NOT_FOUND
        )