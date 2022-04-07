from rest_framework.serializers import ModelSerializer
from .models import Event


class EventListSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = ['id', 'client', 'support_contact', 'event_date']


class EventDetailSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = ['id', 'client',	'date_created', 'date_updated', 'support_contact', 'contract', 'event_status', 'attendees', 'event_date', 'notes']