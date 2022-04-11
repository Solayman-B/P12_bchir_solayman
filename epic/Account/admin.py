from django.contrib import admin
from .models import TeamUser, Client


@admin.register(TeamUser)
class TeamUserAdmin(admin.ModelAdmin):

    list_display = ("id", "last_name", "first_name", "team")
    list_filter = ("last_name", "first_name", "team")
    search_fields = ("last_name", "email")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ("id", "last_name", "first_name", "email", "company_name")
    list_filter = ("last_name", "email")
    search_fields = ("last_name", "email")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_contact":
            kwargs["queryset"] = TeamUser.objects.filter(team="SALES")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
