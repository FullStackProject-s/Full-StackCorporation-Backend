from django.conf import settings

from drf_spectacular.utils import extend_schema

from rest_framework import status

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

from authentication.serializers import (
    CookieTokenRefreshSerializer,
    CookieTokenDeleteSerializer,

    TokenObtainSerializerSchema
)
from authentication.views import logger


@extend_schema(responses=TokenObtainSerializerSchema)
class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Overridden simple-jwt class view for set cookie-refresh token.
    """

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Set refresh token for cookie httponly and return access token.
        """

        if response.data.get('refresh'):
            response.set_cookie(
                settings.COOKIE_REFRESH_TOKEN_NAME,
                response.data['refresh'],
                max_age=settings.COOKIE_MAX_AGE,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Refresh access token by refresh-cookie token and return it.
        """

        if response.data.get('refresh'):
            response.set_cookie(
                settings.COOKIE_REFRESH_TOKEN_NAME,
                response.data['refresh'],
                max_age=settings.COOKIE_MAX_AGE,
                httponly=True
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenDeleteView(TokenRefreshView):
    serializer_class = CookieTokenDeleteSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Delete refresh token from cookie. If token already delete return
        400 bad request.
        """
        response.delete_cookie(
            settings.COOKIE_REFRESH_TOKEN_NAME,
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
