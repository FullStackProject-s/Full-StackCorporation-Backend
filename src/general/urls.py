from django.urls import path

from .views import CreateSuperUserView

urlpatterns = [
    path('create-super-user/',
         CreateSuperUserView.as_view()
         )
]
