from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import PasswordForService
from ..serializers import PasswordForServiceSerializer

User = get_user_model()


class PasswordForServiceTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_password_for_service(self):
        url = "/password/service1/"
        data = {"service": "service1", "password": "password123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PasswordForService.objects.count(), 1)
        self.assertEqual(PasswordForService.objects.get().service, "service1")
        self.assertEqual(PasswordForService.objects.get().created_by, self.user)
        self.assertEqual(PasswordForService.objects.get().password, "password123")

    def test_get_password_for_service(self):
        password = PasswordForService.objects.create(
            service="service1", created_by=self.user
        )
        password.password = "password123"
        password.save()

        url = f"/password/{password.service}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PasswordForServiceSerializer(password).data)

    def test_get_passwords_with_part_of_service_name(self):
        password1 = PasswordForService.objects.create(
            service="service1", created_by=self.user
        )
        password1.password = "password123"
        password1.save()

        password2 = PasswordForService.objects.create(
            service="service2", created_by=self.user
        )
        password2.password = "password456"
        password2.save()

        url = "/password/?service_name=service"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(PasswordForServiceSerializer(password1).data, response.data)
        self.assertIn(PasswordForServiceSerializer(password2).data, response.data)
