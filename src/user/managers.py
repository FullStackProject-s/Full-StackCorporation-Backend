from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not password:
            raise ValueError(_('User must have an password'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_("Users must have an email address"))

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if not kwargs.get('is_active'):
            raise ValueError(_('User must be active'))
        if not kwargs.get('is_staff'):
            raise ValueError(_('Superuser must be staff'))
        if not kwargs.get('is_superuser'):
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **kwargs)
