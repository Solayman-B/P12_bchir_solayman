from rest_framework.serializers import ModelSerializer
from .models import TeamUser, Client, Event, Contract

class UserSerializer(ModelSerializer):

	class Meta:
		model = TeamUser
		fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'team',]


class ClientSerializer(ModelSerializer):

	class Meta:
		model = Client
		fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact',]


class EventSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = ['client',	'date_created', 'date_updated', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes',]


class ContractSerializer(ModelSerializer):

	class Meta:
		model = Contract
		fields = ['sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount', 'payement_due']