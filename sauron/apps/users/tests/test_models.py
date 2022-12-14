import pytest

from sauron.apps.users.models import User


pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User) -> None:
    assert user.get_absolute_url() == f"/api/users/{user.id}/"
