from general.models.utils import set_image_on_imagefield

from organization.serializers.services import (
    update_projects,
)
from organization.serializers.generic import BaseOrganizationSerializer
from organization.serializers.mixins import UniqueProjectForOrganizationMixin

from user.serializers.user import CustomUserShowSerializer


class OrganizationShowSerializer(BaseOrganizationSerializer):
    owner = CustomUserShowSerializer(read_only=True)
    members = CustomUserShowSerializer(many=True, read_only=True)


class OrganizationShowProjectsSerializer(BaseOrganizationSerializer):
    class Meta(BaseOrganizationSerializer.Meta):
        fields = (
            'pk',
            'organization_name'
        )


class OrganizationSerializer(
    BaseOrganizationSerializer,
    UniqueProjectForOrganizationMixin
):
    class Meta(BaseOrganizationSerializer.Meta):
        fields = (
            'pk',
            'organization_name',
            'organization_avatar',
            'projects',
            'members',
        )

    def validate_projects(self, projects):
        return self._validate_projects_field(projects)

    def to_representation(self, instance):
        return OrganizationShowSerializer(instance).data

    def create(self, validated_data):
        instance = super().create(validated_data)

        user = self.context['request'].user

        instance.owner = user
        instance.members.add(user)
        instance.save()

        set_image_on_imagefield(
            instance.organization_name,
            imagefield=instance.organization_avatar,
        )

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
