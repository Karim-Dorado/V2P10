from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission checks if the user is the project author.
    """
    message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
