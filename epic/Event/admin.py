from django.contrib import admin
from .models import Event
from Account.models import TeamUser


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ("id", "client", "support_contact", "event_status", "event_date")
    list_filter = ("client_id__last_name", "client_id__email", "date_created")
    search_fields = ("client_id__last_name", "client_id__email", "date_created")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "support_contact":
            kwargs["queryset"] = TeamUser.objects.filter(team="SUPPORT")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
