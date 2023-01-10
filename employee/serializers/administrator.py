from employee.serializers.generics import BaseAdministratorSerializer

from user.serializers import ProfileShowSerializer


class AdministratorShowSerializer(BaseAdministratorSerializer):
    profile = ProfileShowSerializer(required=False, read_only=True)


class AdministratorSerializer(BaseAdministratorSerializer):
    def to_representation(self, instance):
        return AdministratorShowSerializer(instance).data
