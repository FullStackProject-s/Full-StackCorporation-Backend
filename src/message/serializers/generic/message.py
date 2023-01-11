from rest_framework import serializers


class BaseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'creator',
            'text',
            'create_at',
        )
