from rest_framework.viewsets import ModelViewSet
from Epic.permissions import (
    IsSupportAuthenticated,
    IsSalesAuthenticated,
    IsManagementAuthenticated,
)
from .models import Contract
from .serializers import ContractListSerializer, ContractDetailSerializer


class ContractViewset(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [
        IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated
    ]
    filterset_fields = ["date_created", "date_updated", "amount"]
    search_fields = ["date_created", "date_updated", "amount"]

    def get_queryset(self):
        return Contract.objects.all()

    def get_serializer_class(self):
        if self.action != "list":
            return self.detail_serializer_class
        return super().get_serializer_class()
