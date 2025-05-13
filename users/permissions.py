from rest_framework.permissions import BasePermission


class IsBookingOwnerOrAdmin(BasePermission):
    """Permission to check if the user is the owner of the booking or an admin.

    This permission allows access if the user is authenticated and is the
    owner of the booking or is a staff member.
    """

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to access the object."""
        return ((request.user.is_authenticated) and (
            obj.user == request.user)) or (request.user.is_staff)
