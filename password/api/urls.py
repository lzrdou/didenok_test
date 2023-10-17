from django.urls import path, include
from rest_framework.routers import SimpleRouter

from djoser.views import UserViewSet

from api.views import PasswordForServiceView, PasswordForServiceListView

app_name = "api"

router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path(
        "password/<str:service_name>/",
        PasswordForServiceView.as_view(),
        name="password-detail",
    ),
    path("password/", PasswordForServiceListView.as_view(), name="password-list"),
    path("", include(router.urls)),
]
