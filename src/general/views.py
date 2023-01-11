from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from user.models import CustomUser

"""
ONLY FOR DEVELOPMENT
"""


class CreateSuperUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if not CustomUser.objects.filter(username='bol4onok').exists():
            CustomUser.objects.create_superuser(
                username='bol4onok',
                password='bol4onok',
                email='email@mail.com',
                first_name='1',
                last_name='2'
            )
        return Response()
