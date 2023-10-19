from django.urls import path

from .views import PasswordForServiceListView, PasswordForServiceView

app_name = "api"

urlpatterns = [
    path("password/", PasswordForServiceListView.as_view(), name="password-list"),
    path(
        "password/<str:service>/",
        PasswordForServiceView.as_view(),
        name="password-detail",
    ),
]
