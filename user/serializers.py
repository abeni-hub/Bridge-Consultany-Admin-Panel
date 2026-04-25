from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    is_admin_user = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin_user']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin_user', False)

        user = User.objects.create_user(**validated_data)

        if is_admin:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        return user


# ✅ NEW → for listing users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']