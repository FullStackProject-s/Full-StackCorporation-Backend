from drf_spectacular.utils import extend_schema

from employee.models import Developer
from employee.serializers import (
    DeveloperSerializer,
    DeveloperShowSerializer
)
from employee.views.generics.base_employee import (
    BaseConfigurationEmployeeViewGeneric
)


@extend_schema(responses=DeveloperShowSerializer)
class BaseConfigurationDevelopersViewGeneric(
    BaseConfigurationEmployeeViewGeneric
):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
