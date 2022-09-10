import pytest
from rest_framework.test import APIRequestFactory

from sauron.apps.users.api.views import UserViewSet
from sauron.apps.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, arf: APIRequestFactory):
        view = UserViewSet()
        request = arf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, arf: APIRequestFactory):
        view = UserViewSet()
        request = arf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "avatar": user.avatar,
            "language": user.language,
            "theme": user.theme,
            "url": f"/api/users/{user.id}/",
        }
