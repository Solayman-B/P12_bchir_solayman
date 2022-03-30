import pytest

from django.urls import reverse
from django.test import Client
from .models import TeamUser
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_book_infos_view():
    client = Client()
    TeamUser.objects.create(password = "Azerty23°/",
                        username = "pytest", team = "Support")
    path = reverse('infos', kwargs={'pk':1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = ""

    assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "admin/application/teamuser/add/")