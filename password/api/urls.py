from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PasswordForServiceView, PasswordForServiceListView

app_name = "api"

router = SimpleRouter()

urlpatterns = [
    path("password/", PasswordForServiceListView.as_view(), name="password-list"),
    path(
        "password/<str:service_name>/",
        PasswordForServiceView.as_view(),
        name="password-detail",
    ),
    path("", include(router.urls)),
]
