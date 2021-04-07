from rest_framework import permissions
import re


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj == request.user or request.user.role


class AdminOnly(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        return request.method in self.allowed_methods and request.user.role


class SelfOnlyOrder(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if re.search(fr"{request.user.id}+(?=\/order\/)", request.path):
            return request.method in self.allowed_methods
        return False
