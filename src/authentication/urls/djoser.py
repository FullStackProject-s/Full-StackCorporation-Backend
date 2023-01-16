from rest_framework.routers import DefaultRouter

from authentication.views import djoser

router = DefaultRouter()
router.register("users", djoser.CustomUserViewSet)

urlpatterns_djoser = router.urls
