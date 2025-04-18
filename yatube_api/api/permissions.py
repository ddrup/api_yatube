from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsContentAuthorOrReadOnly(BasePermission):
    """Класс для проверки прав доступа к объектам."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
