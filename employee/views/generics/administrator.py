from employee.models import Administrator
from employee.serializers import AdministratorSerializer


class BaseConfigurationAdministratorsViewGeneric:
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
