import pytest
from django.test.client import Client
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_swagger_accessible_by_admin(admin_client: Client) -> None:
    url = reverse("api-docs")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_swagger_ui_not_accessible_by_normal_user(client: Client) -> None:
    url = reverse("api-docs")
    response = client.get(url)
    assert response.status_code == 403


def test_api_schema_generated_successfully(admin_client: Client) -> None:
    url = reverse("api-schema")
    response = admin_client.get(url)
    assert response.status_code == 200
