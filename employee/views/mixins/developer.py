from employee.models import Developer
from employee.serializers import DeveloperSerializer


class BaseConfigurationDevelopersViewMixin:
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
