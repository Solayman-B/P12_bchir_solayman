from django.db import models
from Account.models import TeamUser, Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        TeamUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Vendeur(se)",
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    date_created = models.DateField(auto_now_add=True, verbose_name="Date de création")
    date_updated = models.DateField(auto_now=True, verbose_name="Date de modification")
    status = models.BooleanField(default=False, verbose_name="Contrat signé")
    amount = models.FloatField(verbose_name="Montant €")
    payement_due = models.DateField(verbose_name="Date d'échéance du paiement")
