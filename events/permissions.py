from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEventOwnerOrAdmin(BasePermission):
    """Permission to check if the user is the owner of the Event or an admin.

    This permission allows access if the user is authenticated and is the
    owner of the Event or is a staff member.
    """

    def has_permission(self, request, view):
        """check before object-specific check"""

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Object-specific permission check"""
        if request.method in SAFE_METHODS:
            return True

        return obj.creator == request.user or request.user.is_staff
