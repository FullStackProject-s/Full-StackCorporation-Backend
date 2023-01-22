from django.urls import path

from general import views

urlpatterns = [
    path('create-super-user/',
         views.CreateSuperUserView.as_view()
         ),
    path(
        'create-fill-data/',
        views.CreateFillDataView.as_view(),

    )
]
