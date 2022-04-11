from rest_framework import permissions
from rest_framework.permissions import BasePermission
from Event.models import Event


class IsSupportAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.team == "SUPPORT"

    def has_object_permission(self, request, view, obj):
        if type(obj) is Event:
            if request.user.id == obj.support_contact.id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS
        else:
            return request.method in permissions.SAFE_METHODS


class IsSalesAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.team == "SALES"

    def has_object_permission(self, request, view, obj):
        if type(obj) is Event:
            if request.user.id == obj.client.sales_contact.id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS
        else:
            if request.user.id == obj.sales_contact.id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS


class IsManagementAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.team == "MANAGEMENT"

    def has_object_permission(self, request, view, obj):
        return request.user.team == "MANAGEMENT"
