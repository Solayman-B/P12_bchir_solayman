from rest_framework.viewsets import ModelViewSet
from .permissions import IsSupportAuthenticated, IsSalesAuthenticated, IsManagementAuthenticated
from .models import Client, Event, Contract
from .serializers import ClientSerializer, EventSerializer, ContractSerializer


class ClientViewset(ModelViewSet):
	serializer_class = ClientSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]

	def get_queryset(self):
		return Client.objects.all()


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]

	def get_queryset(self):
		return Event.objects.all()


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]

	def get_queryset(self):
		return Contract.objects.all()
