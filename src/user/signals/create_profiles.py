from django.db.models.signals import post_save

from user.models import (
    CustomUser,
    Profile
)

from general.signals import suspending_receiver


@suspending_receiver(post_save, sender=CustomUser)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
