from django.contrib import admin
from .models import TeamUser, Client, Event, Contract


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):

	list_display = ("last_name", "first_name", "team")
	search_fields = ("last_name", "email")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

	list_display = ("last_name", "first_name", "email", "company_name")
	search_fields = ("last_name", "email")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

	list_display = ("client", "support_contact", "event_status", "event_date")
	search_fields = ("client_id__last_name", "client_id__email", "date_created")

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

	list_display = ("client", "sales_contact", "status", "date_created", "date_updated", "amount")
	search_fields = ("date_created", "date_updated", "amount")