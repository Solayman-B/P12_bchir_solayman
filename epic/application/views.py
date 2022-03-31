from rest_framework.viewsets import ModelViewSet
from .permissions import IsSupportAuthenticated, IsSalesAuthenticated, IsManagementAuthenticated
from .models import Client, Event, Contract
from .serializers import ClientSerializer, EventSerializer, ContractSerializer


class ClientViewset(ModelViewSet):
	serializer_class = ClientSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["last_name", "email"]
	search_fields = ["last_name", "email"]

	def get_queryset(self):
		return Client.objects.all()


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["client_id__last_name", "client_id__email", "date_created"]
	search_fields = ["client_id__last_name", "client_id__email", "date_created"]

	def get_queryset(self):
		return Event.objects.all()


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["date_created", "date_updated", "amount"]
	search_fields = ["date_created", "date_updated", "amount"]

	def get_queryset(self):
		return Contract.objects.all()
