from django.db.models.signals import post_save
from django.dispatch import receiver

from employee.models import (
    DeveloperOrganizationSpecialty,
    Developer
)


@receiver(
    post_save,
    sender=DeveloperOrganizationSpecialty
)
def set_specialty_developer(
        sender,
        instance: DeveloperOrganizationSpecialty,
        created,
        **kwargs
):
    if created:
        instance.organization_developer.append_specialties(instance)
