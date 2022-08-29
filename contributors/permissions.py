from rest_framework import permissions


class IsProjectContributor(permissions.BasePermission):
    """
    This permission checks if the user is a project contributor.
    Only a contributor can read a project and hi
    """
    message = "Only a contributor can read a project"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
