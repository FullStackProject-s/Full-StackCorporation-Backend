from drf_spectacular.utils import extend_schema

from employee.models import Administrator
from employee.serializers import (
    AdministratorSerializer,
    AdministratorShowSerializer
)

from employee.views.generics.base_employee import (
    BaseConfigurationEmployeeViewGeneric
)


@extend_schema(responses=AdministratorShowSerializer)
class BaseConfigurationAdministratorsViewGeneric(
    BaseConfigurationEmployeeViewGeneric
):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
