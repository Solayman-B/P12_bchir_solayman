from rest_framework.viewsets import ModelViewSet
from Epic.permissions import (
    IsSupportAuthenticated,
    IsSalesAuthenticated,
    IsManagementAuthenticated,
)
from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer


class EventViewset(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [
        IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated
    ]
    filterset_fields = ["client_id__last_name", "client_id__email", "date_created"]
    search_fields = ["client_id__last_name", "client_id__email", "date_created"]

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action != "list":
            return self.detail_serializer_class
        return super().get_serializer_class()
