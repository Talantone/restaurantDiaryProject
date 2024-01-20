from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsRestaurantOwner(permissions.BasePermission):
    """
    Permission for Owner-only creating of Visit objects
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.restaurant.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission for Owner-only updating and deleting of model objects
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.method in SAFE_METHODS
