from employee.models import Administrator
from employee.serializers.generics import BaseStaffSerializer
from employee.serializers.mixins import StaffPermissionsSetSerializerMixin


from user.models.consts import StaffRole


class AdministratorSerializer(
    BaseStaffSerializer,
    StaffPermissionsSetSerializerMixin

):
    class Meta:
        model = Administrator
        fields = (
            *BaseStaffSerializer.Meta.fields,
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.ADMIN
        )