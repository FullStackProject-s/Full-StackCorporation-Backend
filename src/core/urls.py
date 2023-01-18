from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import (
    path,
    include
)
from django.conf.urls.static import static
from django.views.generic import RedirectView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('user.urls')),

    path('', include('employee.urls')),

    path('', include('project.urls')),

    path('', include('organization.urls')),

    path('', include('message.urls')),

    path('auth/', include('authentication.urls')),

    # ONLY FOR DEVELOPMENT
    path('', include('general.urls')),

]

urlpatterns += [
    path(
        'api-swagger/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),

    path(
        '',
        SpectacularSwaggerView.as_view(),
        name="swagger-ui"
    ),
]
urlpatterns += [
    path(
        'favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))
    )
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
