from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from organization.documents import OrganizationDocument


class OrganizationDocumentSerializer(DocumentSerializer):
    class Meta:
        document = OrganizationDocument
        fields = (
            'id',
            'organization_name',
            'owner',
        )
