from django.db.models.signals import post_save

from general.models.utils import set_image_on_imagefield
from general.signals import suspending_receiver

from organization.models import Organization


@suspending_receiver(post_save, sender=Organization)
def create_organization_avatar(
        sender,
        instance: Organization,
        created,
        **kwargs
):
    if created:
        set_image_on_imagefield(
            instance.organization_name,
            imagefield=instance.organization_avatar,
        )
