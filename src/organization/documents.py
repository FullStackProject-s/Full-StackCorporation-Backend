from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from organization.models import (
    Organization,
)
from user.models import (
    CustomUser
)

organization_index = Index('organizations')

organization_index.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@organization_index.doc_type
class OrganizationDocument(Document):
    organization_name = fields.TextField(
        attr='organization_name',
        fields={
            "raw": {
                'type': 'keyword'
            },
            'suggest': fields.Completion(),
        }
    )
    owner = fields.ObjectField(
        properties={
            'username': fields.TextField(
                fields={
                    'raw': {
                        'type': 'keyword',

                    }
                }
            ),
            'first_name': fields.TextField(fields={
                'raw': {
                    'type': 'keyword',

                }
            }),
            'last_name': fields.TextField(fields={
                'raw': {
                    'type': 'keyword',

                }
            }),
        }
    )

    class Django:
        model = Organization
        fields = [
            'id',
            'organization_avatar',
            # 'description',
            # 'type',
        ]

        related_models = (
            CustomUser,
        )

    def get_queryset(self):
        return super().get_queryset().select_related(
            'owner'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, CustomUser):
            return related_instance.organization_set.all()
