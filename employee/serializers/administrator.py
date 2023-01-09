from employee.models import Administrator
from employee.serializers.generics import BaseStaffSerializer

from user.serializers import ProfileShowSerializer


# from employee.serializers.mixins import StaffPermissionsSetSerializerMixin
#
#
# from user.models.consts import StaffRole
#

class BaseAdministratorSerializer(BaseStaffSerializer):
    class Meta:
        model = Administrator
        fields = (
            *BaseStaffSerializer.Meta.fields,
        )


class AdministratorShowSerializer(BaseAdministratorSerializer):
    profile = ProfileShowSerializer(required=False, read_only=True)


class AdministratorSerializer(BaseAdministratorSerializer):
    def to_representation(self, instance):
        return AdministratorShowSerializer(instance).data
