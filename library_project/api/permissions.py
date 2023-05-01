from rest_framework import permissions
from catalog.models import Author


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        current_user = Author.objects.get(user=request.user)
        return obj.author == current_user
