from rest_framework import serializers
from employee.models.employees import Developer
from user.serializers.profile import ProfileSerializer
from employee.serializers.technologies import TechnologiesSerializer


class DeveloperSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    stack = TechnologiesSerializer(many=True)

    class Meta:
        model = Developer
        fields = (
            'profile',
            'specialty',
            'stack',
        )
