class ProfileUpdateSerializerMixin:
    def _profile_update(self, instance, validated_data):
        profile_serializer = self.fields['profile']
        if data := validated_data.pop('profile', None):
            profile_serializer.update(instance.profile, data)