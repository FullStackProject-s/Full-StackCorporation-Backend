from general.models.utils import set_image_on_imagefield
from organization.serializers.services import (
    update_projects,
    create_projects
)
from organization.serializers.generic import BaseOrganizationSerializer

from user.serializers.user import CustomUserShowSerializer

from project.serializer import ProjectShowSerializer


class OrganizationShowSerializer(BaseOrganizationSerializer):
    owner = CustomUserShowSerializer(read_only=True)
    projects = ProjectShowSerializer(many=True, read_only=True)
    members = CustomUserShowSerializer(many=True, read_only=True)


class OrganizationSerializer(BaseOrganizationSerializer):
    class Meta(BaseOrganizationSerializer.Meta):
        fields = (
            'pk',
            'organization_name',
            'organization_avatar',
            'projects',
            'members',
        )

    def to_representation(self, instance):
        return OrganizationShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.owner = self.context['request'].user
        instance.save()

        set_image_on_imagefield(
            instance.organization_name,
            imagefield=instance.organization_avatar,
        )

        create_projects(instance)
        return instance

    def update(self, instance, validated_data):
        update_projects(instance, validated_data)
        return super().update(instance, validated_data)


class OrganizationImageUploadSerializer(BaseOrganizationSerializer):
    class Meta:
        model = BaseOrganizationSerializer.Meta.model
        fields = (
            'organization_avatar',
        )
