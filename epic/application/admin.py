from django.contrib import admin
from .models import TeamUser, Client, Event, Contract


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):

	list_display = ("last_name", "first_name", "team")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

	list_display = ("last_name", "first_name", "company_name")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

	list_display = ("client", "support_contact", "event_status", "event_date")

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

	list_display = ("client", "sales_contact", "status")