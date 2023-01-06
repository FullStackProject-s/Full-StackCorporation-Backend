from employee.models import Developer
from employee.serializers import DeveloperSerializer


class BaseConfigurationDevelopersViewGeneric:
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
