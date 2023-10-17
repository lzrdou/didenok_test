from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PasswordForServiceListView, PasswordForServiceView

app_name = "api"

router = SimpleRouter()

urlpatterns = [
    path("password/", PasswordForServiceListView.as_view(), name="password-list"),
    path(
        "password/<str:service>/",
        PasswordForServiceView.as_view(),
        name="password-detail",
    ),
    path("", include(router.urls)),
]
