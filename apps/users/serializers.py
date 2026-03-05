from rest_framework import serializers
from apps.users.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'full_name', 'role', 'age', 'avatarka', 'gender')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'full_name', 'role', 'age', 'avatarka', 'gender')
        read_only_fields = ('username', 'role')

class TokenResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField(help_text="JWT refresh token")
    access = serializers.CharField(help_text="JWT access token")