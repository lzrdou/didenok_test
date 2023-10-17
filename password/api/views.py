from rest_framework import generics

from .models import PasswordForService
from .permissions import IsAuthorOrCreateOnly
from .serializers import PasswordForServiceSerializer


class PasswordForServiceView(
    generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView
):
    serializer_class = PasswordForServiceSerializer
    lookup_field = "service"
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service_name = self.kwargs["service"]
        return PasswordForService.objects.filter(service=service_name)

    def perform_create(self, serializer):
        service_name = self.kwargs["service"]
        serializer.save(created_by=self.request.user, service=service_name)

    def perform_update(self, serializer):
        instance = serializer.instance
        instance.password = serializer.validated_data.get("password", instance.password)
        instance.save()


class PasswordForServiceListView(generics.ListAPIView):
    serializer_class = PasswordForServiceSerializer
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service_name = self.request.query_params.get("service", "")
        return PasswordForService.objects.filter(service__icontains=service_name)
