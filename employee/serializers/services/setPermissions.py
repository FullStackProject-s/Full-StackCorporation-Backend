from user.models import CustomUser


class SetUserPermission:
    @staticmethod
    def set_permissions(username, permission):
        c = CustomUser.objects.get(username=username)
        c.staff_role = permission
        c.save()

