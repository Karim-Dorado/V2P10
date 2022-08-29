from rest_framework import permissions


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission checks if the user is the comment author.
    Only the author can update or delete a comment.
    """
    message = "Only the author can update or delete this comment"

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
