from rest_framework.viewsets import ModelViewSet
from Epic.permissions import IsSupportAuthenticated, IsSalesAuthenticated, IsManagementAuthenticated
from .models import Client
from .serializers import ClientSerializer


class ClientViewset(ModelViewSet):
	serializer_class = ClientSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["last_name", "email"]
	search_fields = ["last_name", "email"]

	def get_queryset(self):
		return Client.objects.all()