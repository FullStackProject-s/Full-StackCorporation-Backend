from django.contrib.auth import get_user_model

from user.models import Profile

User = get_user_model()


class CreateCustomUserSerializerMixin:

    def _create_user(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
        )
        return user

    def _create_profile(self, validated_data):
        _user = self._create_user(validated_data.pop('user'))
        _profile = Profile.objects.create(**validated_data, user=_user)
        return _profile

