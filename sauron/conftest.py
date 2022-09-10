import pytest
from rest_framework.test import APIRequestFactory

from sauron.apps.users.models import User
from sauron.apps.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def arf() -> APIRequestFactory:
    return APIRequestFactory(enforce_csrf_checks=True)
