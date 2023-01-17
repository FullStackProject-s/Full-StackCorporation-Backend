from django.conf import settings
from rest_framework import status, serializers
from rest_framework.exceptions import NotFound

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)
from authentication.serializers import (
    CookieTokenRefreshSerializer,
    CookieTokenDeleteSerializer
)


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


class CookieTokenDeleteView(TokenRefreshView):
    serializer_class = CookieTokenDeleteSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.delete_cookie(
            'refresh_token',
        )
        if not request.COOKIES.get('refresh_token'):
            response.data['detail'] = 'Refresh token already delete'
            response.status_code = status.HTTP_400_BAD_REQUEST
            return super().finalize_response(
                request,
                response,
                *args,
                **kwargs
            )
        response.status_code = status.HTTP_204_NO_CONTENT
        return super().finalize_response(request, response, *args, **kwargs)
