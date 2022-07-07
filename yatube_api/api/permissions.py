from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    message = 'Вы не авторизованы.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True
