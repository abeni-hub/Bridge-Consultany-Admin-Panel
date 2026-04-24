from rest_framework.permissions import BasePermission, SAFE_METHODS


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        # Allow GET, POST, PATCH for everyone
        if request.method in ['GET', 'POST', 'PATCH', 'PUT']:
            return True

        # DELETE only admin
        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        return False