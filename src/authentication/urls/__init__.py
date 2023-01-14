from django.urls import path
from authentication.views import (
    login,
    token
)

urlpatterns = [
    path('login/', login.LoginView.as_view(), name="login"),

    path(
        'token/',
        token.CookieTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        token.CookieTokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
