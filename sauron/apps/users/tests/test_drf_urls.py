import pytest
from django.urls import resolve, reverse

from sauron.apps.users.models import User


pytestmark = pytest.mark.django_db


def test_user_detail(user: User) -> None:
    assert (
        reverse("api:user-detail", kwargs={"id": user.id})
        == f"/api/users/{user.id}/"
    )
    assert resolve(f"/api/users/{user.id}/").view_name == "api:user-detail"


def test_user_list() -> None:
    assert reverse("api:user-list") == "/api/users/"
    assert resolve("/api/users/").view_name == "api:user-list"


def test_user_me() -> None:
    assert reverse("api:user-me") == "/api/users/me/"
    assert resolve("/api/users/me/").view_name == "api:user-me"
