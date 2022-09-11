import typing

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from allauth.account.views import LogoutFunctionalityMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.db import models
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, RedirectView, UpdateView


if typing.TYPE_CHECKING:
    from sauron.apps.users.models import User
else:
    User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):  # type: ignore[type-arg]
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


class UserUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,  # type: ignore[type-arg]
):
    model = User
    fields = ["username"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self) -> "User":  # type: ignore[override]
        # False positive on AnonymousUser from mypy
        return self.request.user  # type: ignore[return-value]


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:  # type: ignore[override]
        return reverse(
            "users:detail",
            kwargs={"id": self.request.user.id},
        )


# Allauth Rewritten Views
# =============================================================================
class ConfirmEmailView(LogoutFunctionalityMixin, View):  # type: ignore[misc]
    object: EmailConfirmationHMAC | None

    def get(
        self, *args: typing.Any, **kwargs: dict[str, typing.Any]
    ) -> HttpResponse:
        try:
            self.object = self.get_object()
            return self.post(*args, **kwargs)
        except Http404:
            self.object = None

        return redirect("vue:account_invalid_email")

    def post(
        self, *args: typing.Any, **kwargs: dict[str, typing.Any]
    ) -> HttpResponse:
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        if (
            self.request.user.is_authenticated
            and self.request.user.pk != confirmation.email_address.user_id
        ):
            self.logout()

        return redirect(self.get_redirect_url())

    def get_object(
        self, queryset: models.QuerySet[EmailConfirmation] | None = None
    ) -> EmailConfirmationHMAC:
        key = self.kwargs["key"]
        email_confirmation = EmailConfirmationHMAC.from_key(key)

        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                raise Http404()

        return email_confirmation

    @staticmethod
    def get_queryset() -> models.QuerySet[EmailConfirmation]:
        qs: models.QuerySet[
            EmailConfirmation
        ] = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs

    def get_context_data(
        self, **kwargs: dict[str, typing.Any]
    ) -> dict[str, typing.Any]:
        ctx: dict[str, typing.Any] = kwargs
        ctx["confirmation"] = self.object

        site = get_current_site(self.request)
        ctx.update({"site": site})

        return ctx

    def get_redirect_url(self) -> str:
        return (
            get_adapter(self.request).get_email_confirmation_redirect_url(
                self.request
            )
            or "home"
        )
