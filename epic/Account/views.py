from rest_framework.viewsets import ModelViewSet
from Epic.permissions import (
    IsSupportAuthenticated,
    IsSalesAuthenticated,
    IsManagementAuthenticated,
)
from .models import Client, TeamUser
from .serializers import (
    TeamUserListSerializer,
    TeamUserDetailSerializer,
    ClientListSerializer,
    ClientDetailSerializer,
)


class TeamUserViewset(ModelViewSet):
    serializer_class = TeamUserListSerializer
    detail_serializer_class = TeamUserDetailSerializer
    permission_classes = [IsManagementAuthenticated]
    filterset_fields = ["last_name", "team"]
    search_fields = ["last_name", "team"]

    def get_queryset(self):
        return TeamUser.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewset(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [
        IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated
    ]
    filterset_fields = ["last_name", "email"]
    search_fields = ["last_name", "email"]

    def get_queryset(self):
        return Client.objects.all()

    def get_serializer_class(self):
        if self.action != "list":
            return self.detail_serializer_class
        return super().get_serializer_class()
