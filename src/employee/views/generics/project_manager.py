from drf_spectacular.utils import extend_schema

from employee.models import ProjectManager
from employee.serializers import (
    ProjectManagerSerializer,
    ProjectManagerShowSerializer
)
from employee.views.generics.base_employee import (
    BaseConfigurationEmployeeViewGeneric
)


@extend_schema(responses=ProjectManagerShowSerializer)
class BaseConfigurationProjectManagersViewGeneric(
    BaseConfigurationEmployeeViewGeneric
):
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()
