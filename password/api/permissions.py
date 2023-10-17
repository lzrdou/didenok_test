from rest_framework import permissions


class IsAuthorOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "PATCH"]:
            return True
        return obj.created_by == request.user
