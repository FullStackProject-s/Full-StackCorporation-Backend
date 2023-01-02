from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('api-swagger/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('docs/', SpectacularSwaggerView.as_view(),
         name="swagger-ui"),
]