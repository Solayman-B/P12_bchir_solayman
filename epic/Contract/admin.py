from django.contrib import admin
from .models import Contract
from Account.models import TeamUser


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "client",
        "sales_contact",
        "status",
        "date_created",
        "date_updated",
        "amount",
    )
    list_filter = ("date_created", "date_updated", "amount")
    search_fields = ("date_created", "date_updated", "amount")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_contact":
            kwargs["queryset"] = TeamUser.objects.filter(team="SALES")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
