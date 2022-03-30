from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import TeamUser, Event

class IsSupportAuthenticated(BasePermission):

	def has_permission(self, request, view):
		support_user = TeamUser.objects.filter(team="Support")
		return request.user in support_user.all()

	def has_object_permission(self, request, view, obj):
		if type (obj) is Event:
			if request.user.id == obj.support_contact.id:
				return True
			else:
				return request.method in permissions.SAFE_METHODS
		else:
			return request.method in permissions.SAFE_METHODS


class IsSalesAuthenticated(BasePermission):

	def has_permission(self, request, view):
		support_user = TeamUser.objects.filter(team="Ventes")
		return request.user in support_user.all()

	def has_object_permission(self, request, view, obj):
		if type (obj) is Event:
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
		management_user = TeamUser.objects.filter(team="Gestion")
		return request.user in management_user

	def has_object_permission(self, request, view, obj):
		management_user = TeamUser.objects.filter(team="Gestion")
		return request.user in management_user