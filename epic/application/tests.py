from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from .models import TeamUser, Client, Event, Contract

class TestClient(APITestCase):
    url = reverse_lazy('client')