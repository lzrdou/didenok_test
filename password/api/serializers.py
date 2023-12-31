from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from .models import PasswordForService, User


class UserSerializer(BaseUserSerializer):
    """Общий сериализатор модели User."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class UserCreateSerializer(BaseUserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = User
        fields = ("username", "password")


class UserCreateResponseSerializer(UserSerializer):
    """Сериализатор для ответа при создании пользователя."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class PasswordForServiceSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = PasswordForService
        fields = ("service", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = super().create(validated_data)
        instance.password = password
        instance.save()
        return instance


class PasswordForServiceResponseSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = PasswordForService
        fields = ("password",)
