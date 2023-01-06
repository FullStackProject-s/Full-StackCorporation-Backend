from employee.models import Administrator
from employee.serializers import AdministratorSerializer


class BaseConfigurationAdministratorsViewMixin:
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
