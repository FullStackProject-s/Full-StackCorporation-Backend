from django.db.models.signals import post_save
from django.dispatch import receiver

from general.models.utils import set_image_on_imagefield
from user.models import (
    CustomUser,
    Profile
)

from general.signals import suspending_receiver


@suspending_receiver(post_save, sender=CustomUser)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def set_avatar_for_profile(sender, instance, created, **kwargs):
    if created:
        set_image_on_imagefield(
            instance.user.username,
            instance.user.email,
            imagefield=instance.profile_avatar,
        )
