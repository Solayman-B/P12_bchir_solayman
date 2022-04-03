from rest_framework.viewsets import ModelViewSet
from Epic.permissions import IsSupportAuthenticated, IsSalesAuthenticated, IsManagementAuthenticated
from .models import Event
from .serializers import EventSerializer


class EventViewset(ModelViewSet):
	serializer_class = EventSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["client_id__last_name", "client_id__email", "date_created"]
	search_fields = ["client_id__last_name", "client_id__email", "date_created"]

	def get_queryset(self):
		return Event.objects.all()