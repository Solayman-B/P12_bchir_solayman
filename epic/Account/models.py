from django.db import models
from django.contrib.auth.models import AbstractUser


class TeamUser(AbstractUser):
    TEAM_CHOICES = (
        ("SUPPORT", "Support"),
        ("SALES", "Ventes"),
        ("MANAGEMENT", "Gestion"),
    )

    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone"
    )
    mobile = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Portable"
    )
    team = models.CharField(
        max_length=20, choices=TEAM_CHOICES, blank=True, null=True, verbose_name="Pôle"
    )


class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Prénom")
    last_name = models.CharField(max_length=25, verbose_name="Nom")
    email = models.EmailField(
        max_length=100, blank=True, null=True, verbose_name="Courriel"
    )
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone"
    )
    mobile = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Portable"
    )
    company_name = models.CharField(max_length=250, verbose_name="Entreprise")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="Date d'inscription"
    )
    date_updated = models.DateField(auto_now=True, verbose_name="Date de modification")
    sales_contact = models.ForeignKey(
        TeamUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Vendeur(se)",
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
