import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_object_debt_url(client):
    response = client.get(reverse("object_debt"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_country_url(client):
    response = client.get(reverse("country", kwargs={"country": "BY"}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_url(client):
    response = client.get(reverse("product", kwargs={"product": "Snikers"}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_object_url(client):
    response = client.get(reverse("object"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_object_url(client):
    response = client.get(reverse("object"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_send_email_url(client):
    response = client.get(reverse("send"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_contacts_url(client):
    response = client.get(reverse("contacts"))
    assert response.status_code == 200
