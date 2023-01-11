from django.contrib import admin
from .models import *

admin.site.register(Developer)
admin.site.register(ProjectManager)
admin.site.register(Administrator)
admin.site.register(Technologies)
admin.site.register(DeveloperOrganizationSpecialty)