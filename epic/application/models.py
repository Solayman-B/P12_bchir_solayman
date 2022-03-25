from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	SUPPORT = 'Support'
	SALES = 'Ventes'
	MANAGEMENT = 'Gestion'

	TEAM_CHOICES = ((SUPPORT, 'Support'),
					(SALES, 'Ventes'),
					(MANAGEMENT, 'Gestion'),
					)

	phone = models.CharField(max_length=20, blank=True, null=True)
	mobile = models.CharField(max_length=20, blank=True, null=True)
	team = models.CharField(max_length=20, choices=TEAM_CHOICES)

	def __str__(self):
		return f'{self.first_name} {self.last_name} team {self.team}'

class Client(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	mobile = models.CharField(max_length=20, blank=True, null=True)
	company_name = models.CharField(max_length=250)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	sales_contact = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name} {self.company_name}'


class Event(models.Model):
	CREATED = "Créé"
	ASSIGNED = "Affecté"
	FINISHED = "Terminé"

	EVENT_CHOICES = ((CREATED, "Créé"),
					 (ASSIGNED, "Affecté"),
					 (FINISHED, "Terminé"),
					 )

	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now_add=True)
	support_contact = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	event_status = models.CharField(max_length=20, choices=EVENT_CHOICES)
	attendees = models.IntegerField()
	event_date = models.DateField()
	notes = models.TextField()

	def __str__(self):
		return f'{self.client} {self.event_status}'


class Contract(models.Model):
	sales_contact = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	status = models.BooleanField(default=False)
	amount = models.FloatField()
	payement_due = models.DateField()

	def __str__(self):
		return f'{self.client} {self.status}'