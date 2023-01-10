from django.db import models


class BaseTimeStampModel(models.Model):
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
