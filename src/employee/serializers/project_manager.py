from employee.serializers.generics import BaseProjectManagerSerializer
from employee.serializers.services import set_perms_for_employee

from user.models.consts import StaffRole
from user.serializers import ProfileShowSerializer


class ProjectManagerShowSerializer(BaseProjectManagerSerializer):
    profile = ProfileShowSerializer(required=False, read_only=True)


class ProjectManagerSerializer(BaseProjectManagerSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        set_perms_for_employee(StaffRole.PRODUCT_MANAGER, instance)
        return instance

    def to_representation(self, instance):
        return ProjectManagerShowSerializer(instance).data
