from employee.models import ProjectManager
from employee.serializers import ProjectManagerSerializer


class BaseConfigurationProjectManagersViewGeneric:
    serializer_class = ProjectManagerSerializer
    queryset = ProjectManager.objects.all()
