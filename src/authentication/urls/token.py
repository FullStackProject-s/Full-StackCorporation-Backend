from django.urls import path

from authentication.views import token

urlpatterns_token = [
    path(
        'tokens-obtain/',
        token.CookieTokenObtainPairView.as_view(),
        name='token-obtain-pair'
    ),
    path(
        'refresh/',
        token.CookieTokenRefreshView.as_view(),
        name='token-refresh'
    ),
    path(
        'delete/',
        token.CookieTokenDeleteView.as_view(),
        name='token-delete',
    )

]
