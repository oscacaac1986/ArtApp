from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Permits the use of HTTTP's safe methods for any user, and restricts the
    usage of the remaining ones to staff members."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff