from rest_framework import generics, status
from rest_framework.response import Response

from .models import PasswordForService
from .permissions import IsAuthorOrCreateOnly
from .serializers import (
    PasswordForServiceSerializer,
    PasswordForServiceResponseSerializer,
)


class PasswordForServiceView(
    generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView
):
    serializer_class = PasswordForServiceSerializer
    lookup_field = "service"
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service = self.kwargs["service"]
        return PasswordForService.objects.filter(service=service)

    def create(self, request, *args, **kwargs):
        service = self.kwargs["service"]
        data = request.data
        data["service"] = service
        if PasswordForService.objects.filter(service=service).exists():
            obj = PasswordForService.objects.get(service=service)
            obj.password = data["password"]
            obj.save()
            headers = self.get_success_headers(data)
            del data["service"]
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PasswordForServiceResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        instance.password = serializer.validated_data.get("password", instance.password)
        instance.save()


class PasswordForServiceListView(generics.ListAPIView):
    serializer_class = PasswordForServiceSerializer
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service_name = self.request.query_params.get("service_name", "")
        if service_name:
            return PasswordForService.objects.filter(service__icontains=service_name, created_by=self.request.user)
        return PasswordForService.objects.none()
