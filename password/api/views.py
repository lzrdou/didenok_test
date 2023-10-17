from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.db.models import Q

from .models import PasswordForService
from .permissions import IsCreatedByOrReadOnly
from .serializers import PasswordForServiceSerializer


class PasswordForServiceView(generics.RetrieveAPIView):
    serializer_class = PasswordForServiceSerializer
    lookup_field = "service"
    permission_classes = [IsCreatedByOrReadOnly]

    def get_queryset(self):
        return PasswordForService.objects.all()

    def get_object(self):
        service_name = self.kwargs["service_name"]
        queryset = self.filter_queryset(self.get_queryset())
        try:
            obj = queryset.get(service=service_name)
        except ObjectDoesNotExist:
            raise NotFound("PasswordForService not found.")
        self.check_object_permissions(self.request, obj)
        return obj


class PasswordForServiceListView(generics.ListCreateAPIView):
    serializer_class = PasswordForServiceSerializer
    permission_classes = [IsCreatedByOrReadOnly]

    def get_queryset(self):
        service_name = self.request.query_params.get("service_name", "")
        return PasswordForService.objects.filter(service__icontains=service_name)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
