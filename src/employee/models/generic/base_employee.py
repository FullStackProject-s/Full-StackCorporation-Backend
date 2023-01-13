from django.db import models
from user.models.profile import Profile


class BaseEmployeeGeneric(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class BaseProjectManagerDeveloperGeneric(BaseEmployeeGeneric):
    class Meta:
        abstract = True

    def set_team(self, team):
        self.team = team
        self.save()

    def remove_team(self):
        self.team = None
        self.save()
