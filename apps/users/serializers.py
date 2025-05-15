from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    role = serializers.CharField(source='get_role_display')

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'role',
            'profile_picture',
            'created_at',
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials')
        return {
            'user': user,
        }
