from rest_framework import serializers

from user.models.utility import Permissions


class PermissionSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(
        source='get_role_name_display',
        read_only=True
    )

    class Meta:
        model = Permissions
        fields = (
            'pk',
            'role_name',
        )