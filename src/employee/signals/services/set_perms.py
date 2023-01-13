from django.contrib.auth import get_user_model

User = get_user_model()


def set_perms_for_employee(instance, perms):
    user = User.objects.get(pk=instance.profile.user.pk)
    instance.profile.user.staff_role = perms
    user.staff_role = perms
    instance.save()
    user.save()
