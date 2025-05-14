"""Module for providing permissions for the Event model."""
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Permission to check if the user is the owner of the Event or an admin.

    This permission allows access if the user is authenticated and is the
    owner of the Event or is a staff member.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
