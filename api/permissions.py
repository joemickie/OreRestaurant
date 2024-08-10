from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow any user to view (safe methods) or staff users to modify
        return request.method in permissions.SAFE_METHODS or request.user.is_staff_member
