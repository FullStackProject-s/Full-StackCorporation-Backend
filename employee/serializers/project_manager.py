from employee.models import ProjectManager
from employee.serializers.baseSerializers import BaseManagerDeveloperSerializer
from employee.serializers.mixins import StaffPermissionsSetSerializerMixin


from user.models.consts import StaffRole


class ProjectManagerSerializer(
    BaseManagerDeveloperSerializer,
    StaffPermissionsSetSerializerMixin
):
    class Meta:
        model = ProjectManager
        fields = (
            *BaseManagerDeveloperSerializer.Meta.fields,
        )

    def create(self, validated_data):
        obj = super().create(validated_data)

        return self._set_permissions(
            obj,
            StaffRole.PRODUCT_MANAGER,
        )
