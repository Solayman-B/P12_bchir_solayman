from rest_framework.viewsets import ModelViewSet
from .models import User, Client, Event, Contract
from .serializers import UserSerializer, ClientSerializer, EventSerializer, ContractSerializer


class UserViewset(ModelViewSet):
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.all()


class ClientViewset(ModelViewSet):
	serializer_class = ClientSerializer

	def get_queryset(self):
		return Client.objects.all()


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer

	def get_queryset(self):
		return Event.objects.all()


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer

	def get_queryset(self):
		return Contract.objects.all()
