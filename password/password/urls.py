from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include("api.urls", namespace="api")),
]
