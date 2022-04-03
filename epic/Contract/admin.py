from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

	list_display = ("client", "sales_contact", "status", "date_created", "date_updated", "amount")
	list_filter = ("date_created", "date_updated", "amount")
	search_fields = ("date_created", "date_updated", "amount")