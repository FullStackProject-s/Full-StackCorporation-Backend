from employee.models import Technologies
from employee.serializers import TechnologiesSerializer


class BaseConfigurationTechnologiesViewMixin:
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
