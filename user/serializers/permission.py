from rest_framework import serializers

from user.models.utility import Permissions


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permissions
        fields = (
            'pk',
            'role_name',
        )