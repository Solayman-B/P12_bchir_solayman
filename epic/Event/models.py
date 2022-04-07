from django.db import models
from Account.models import TeamUser, Client
from Contract.models import Contract

class Event(models.Model):
	EVENT_CHOICES = (("CREATED", "Créé"),
					 ("FINISHED", "Terminé"),
					 )

	client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
	date_created = models.DateField(auto_now_add=True, verbose_name="Date de création")
	date_updated = models.DateField(auto_now_add=True, verbose_name="Date de modification")
	support_contact = models.ForeignKey(TeamUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Responsable")
	contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Contrat')
	event_status = models.CharField(max_length=20, choices=EVENT_CHOICES, verbose_name="Statut de l'évènement")
	attendees = models.IntegerField(verbose_name="Nombre de participants")
	event_date = models.DateField(verbose_name="Date de l'évènement")
	notes = models.TextField(blank=True, null=True, verbose_name="Notes")