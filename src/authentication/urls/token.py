from django.urls import path

from authentication.views import token

urlpatterns_token = [
    path(
        'tokens-obtain/',
        token.CookieTokenObtainPairView.as_view(),
        name='token-obtain-pair'
    ),
    path(
        'token/refresh/',
        token.CookieTokenRefreshView.as_view(),
        name='token-refresh'
    ),
    path(
        'token/delete/',
        token.CookieTokenDeleteView.as_view(),
        name='token-delete',
    )

]
