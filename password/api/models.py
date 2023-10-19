import base64

from cryptography.fernet import Fernet
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from password.settings import KEY

cipher_suite = Fernet(KEY)


class User(AbstractUser):
    username_validator = RegexValidator(
        regex=r"^[a-zA-z0-9]", message=("Неверный формат")
    )
    username = models.CharField(
        max_length=150,
        validators=[
            username_validator,
        ],
        unique=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class PasswordForService(models.Model):
    service = models.SlugField(max_length=50, unique=True)
    encrypted_password = models.TextField(db_column="encrypted_password", blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="passwords",
    )

    def get_encrypted_password(self):
        return base64.decodestring(self.encrypted_password)

    class Meta:
        verbose_name = "Пароль для сервиса"
        verbose_name_plural = "Пароли для сервисов"
        unique_together = (
            "service",
            "created_by",
        )

    @property
    def password(self):
        return cipher_suite.decrypt(self.encrypted_password).decode()

    @password.setter
    def password(self, value):
        self.encrypted_password = cipher_suite.encrypt(value.encode()).decode("utf8")
