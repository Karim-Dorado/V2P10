from rest_framework import permissions


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    """
    This permission checks if the user is the comment author.
    Only the author can update or delete a comment.
    """
    message = "Seul l'auteur du commentaire peut actualiser ou supprimer"

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
