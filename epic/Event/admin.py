from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

	list_display = ("id", "client", "support_contact", "event_status", "event_date")
	list_filter = ("client_id__last_name", "client_id__email", "date_created")
	search_fields = ("client_id__last_name", "client_id__email", "date_created")