import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse

from sauron.apps.users.forms import UserAdminChangeForm
from sauron.apps.users.models import User
from sauron.apps.users.tests.factories import UserFactory
from sauron.apps.users.views import (
    UserDetailView,
    UserRedirectView,
    UserUpdateView,
)


pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def dummy_get_response(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(request.body)

    def test_get_success_url(self, user: User, rf: RequestFactory) -> None:
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/api/users/{user.id}/"

    def test_get_object(self, user: User, rf: RequestFactory) -> None:
        view = UserUpdateView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user

    def test_form_valid(self, user: User, rf: RequestFactory) -> None:
        view = UserUpdateView()
        request = rf.get("/fake-url/")

        # Add the session/message middleware to the request
        SessionMiddleware(self.dummy_get_response).process_request(request)
        MessageMiddleware(self.dummy_get_response).process_request(request)
        request.user = user

        view.request = request

        # Initialize the form
        form = UserAdminChangeForm()
        form.cleaned_data = {}
        view.form_valid(form)

        messages_sent = [m.message for m in messages.get_messages(request)]
        assert messages_sent == ["Information successfully updated"]


class TestUserRedirectView:
    def test_get_redirect_url(self, user: User, rf: RequestFactory) -> None:
        view = UserRedirectView()
        request = rf.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/api/users/{user.id}/"


class TestUserDetailView:
    def test_authenticated(self, user: User, rf: RequestFactory) -> None:
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = UserDetailView.as_view()(request, id=user.id)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory) -> None:
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = UserDetailView.as_view()(request, id=user.id)
        login_url = reverse(settings.LOGIN_URL)

        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"
