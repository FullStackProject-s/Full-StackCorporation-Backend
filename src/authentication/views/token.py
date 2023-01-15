from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)
from authentication.serializers import CookieTokenRefreshSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie(
                'refresh_token',
                response.data['refresh'],
                max_age=settings.COOKIE_MAX_AGE,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie(
                'refresh_token',
                response.data['refresh'],
                max_age=settings.COOKIE_MAX_AGE,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)
