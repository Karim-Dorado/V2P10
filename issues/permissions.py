from rest_framework import permissions


class IsIssueAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission checks if the user is the issue author.
    Only the author can update or delete an issue.
    """
    message = "Only the author can update or delete this issue"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
