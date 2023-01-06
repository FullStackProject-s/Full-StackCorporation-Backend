from employee.models import Technologies
from employee.serializers import TechnologiesSerializer


class BaseConfigurationTechnologiesViewGeneric:
    serializer_class = TechnologiesSerializer
    queryset = Technologies.objects.all()
