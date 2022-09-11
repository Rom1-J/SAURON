import pytest
from django.conf import LazySettings
from rest_framework.test import APIRequestFactory

from sauron.apps.users.models import User
from sauron.apps.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)  # type: ignore[misc]
def media_storage(  # type: ignore[no-untyped-def]
    settings: LazySettings, tmpdir
) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture  # type: ignore[misc]
def user(db) -> User:  # type: ignore[no-untyped-def]
    return UserFactory()


@pytest.fixture  # type: ignore[misc]
def arf() -> APIRequestFactory:
    return APIRequestFactory(enforce_csrf_checks=True)
