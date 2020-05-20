from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_admin


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


# class IsGetOrPatchOrPut(permissions.BasePermission):
# 	def has_permission(self, request, view):
# 		allowed_methods = ['GET', 'PATCH', 'PUT']
# 		if request.method in allowed_methods:
# 			return True
# 		else:
# 			return False

class IsLoggedInUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

