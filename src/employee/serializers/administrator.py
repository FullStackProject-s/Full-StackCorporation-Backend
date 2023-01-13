from employee.serializers.generics import BaseAdministratorSerializer
from employee.serializers.services import set_perms_for_employee

from user.models.consts import StaffRole
from user.serializers import ProfileShowSerializer


class AdministratorShowSerializer(BaseAdministratorSerializer):
    profile = ProfileShowSerializer(required=False, read_only=True)


class AdministratorSerializer(BaseAdministratorSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        set_perms_for_employee(StaffRole.ADMIN, instance)
        return instance

    def to_representation(self, instance):
        return AdministratorShowSerializer(instance).data
