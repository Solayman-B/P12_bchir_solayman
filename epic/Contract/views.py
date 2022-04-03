from rest_framework.viewsets import ModelViewSet
from Epic.permissions import IsSupportAuthenticated, IsSalesAuthenticated, IsManagementAuthenticated
from .models import Contract
from .serializers import ContractSerializer


class ContractViewset(ModelViewSet):
	serializer_class = ContractSerializer
	permission_classes = [IsSupportAuthenticated | IsSalesAuthenticated | IsManagementAuthenticated]
	filterset_fields = ["date_created", "date_updated", "amount"]
	search_fields = ["date_created", "date_updated", "amount"]

	def get_queryset(self):
		return Contract.objects.all()
