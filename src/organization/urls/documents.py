from rest_framework.routers import DefaultRouter

from organization.views import documents

router = DefaultRouter()
router.register(
    "documents",
    documents.OrganizationDocumentViewSet,
    basename='organization-document'
)

urlpatterns_document = router.urls
