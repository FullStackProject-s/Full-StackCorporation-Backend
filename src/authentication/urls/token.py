from django.urls import path

from authentication.views import token

urlpatterns_token = [
    path(
        'tokens-obtain/',
        token.CookieTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        token.CookieTokenRefreshView.as_view(),
        name='token_refresh'
    ),

]
