from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import (
    CustomUser,
    Profile
)


@receiver(post_save, sender=CustomUser)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
