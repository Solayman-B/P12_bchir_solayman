from rest_framework.serializers import ModelSerializer
from .models import Contract


class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "sales_contact", "client"]


class ContractDetailSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payement_due",
        ]
