from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        raise InvalidToken(
            'No valid token found in cookie \'refresh_token\''
        )


class CookieTokenDeleteSerializer(TokenRefreshSerializer):
    refresh = None
    access = None

    def validate(self, attrs):
        return attrs
