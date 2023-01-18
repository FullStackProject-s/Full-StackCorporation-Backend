from django.urls import path

from .views import (
    CreateFillDataView,
    CreateSuperUserView
)

urlpatterns = [
    path('create-super-user/',
         CreateSuperUserView.as_view()
         ),
    path(
        'create-fill-data/',
        CreateFillDataView.as_view(),

    )
]
