from rest_framework import serializers


class BaseMessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'pk',
            'creator',
            'text',
            'create_at',
        )
