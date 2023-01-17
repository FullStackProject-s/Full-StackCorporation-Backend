from django.db.models.signals import post_save

from general.models.utils import set_image_on_imagefield
from user.models import (
    CustomUser,
    Profile
)

from general.signals import suspending_receiver


@suspending_receiver(post_save, sender=CustomUser)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        instance_ = Profile.objects.create(user=instance)

        set_image_on_imagefield(
            instance.username,
            instance.email,
            imagefield=instance_.profile_avatar,
        )
