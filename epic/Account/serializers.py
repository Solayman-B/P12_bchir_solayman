from rest_framework.serializers import ModelSerializer
from .models import TeamUser, Client


class TeamUserListSerializer(ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ["id", "first_name", "last_name", "team"]


class TeamUserDetailSerializer(ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ["id", "first_name", "last_name", "email", "phone", "mobile", "team"]


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "company_name", "sales_contact"]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
            "date_created",
            "date_updated",
            "sales_contact",
        ]
