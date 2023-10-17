from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from django.db.models import Q
from rest_framework.response import Response

from .models import PasswordForService
from .permissions import IsAuthorOrCreateOnly
from .serializers import PasswordForServiceSerializer


class PasswordForServiceView(generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = PasswordForServiceSerializer
    lookup_field = 'service'
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service_name = self.kwargs['service_name']
        return PasswordForService.objects.filter(service=service_name)

    def perform_create(self, serializer):
        service_name = self.kwargs['service_name']
        serializer.save(created_by=self.request.user, service=service_name)

    def perform_update(self, serializer):
        instance = serializer.instance
        instance.password = serializer.validated_data.get('password', instance.password)
        instance.save()


class PasswordForServiceListView(generics.ListAPIView):
    serializer_class = PasswordForServiceSerializer
    permission_classes = [IsAuthorOrCreateOnly]

    def get_queryset(self):
        service_name = self.request.query_params.get('service_name', '')
        return PasswordForService.objects.filter(service__icontains=service_name)
