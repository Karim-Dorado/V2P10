from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission checks if the user is the project author.
    """
    message = "Only the author can update or delete a project"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
