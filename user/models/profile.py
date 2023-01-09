from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        'user.CustomUser',
        on_delete=models.CASCADE,
    )
    profile_avatar = models.ImageField(
        upload_to='user_avatar',
        blank=True,
        null=True
    )
    about_user = models.TextField(
        max_length=10_000,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} - {self.pk}'
