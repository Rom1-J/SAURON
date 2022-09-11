import typing
from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):  # type: ignore[misc]
    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("name")

    @post_generation  # type: ignore[misc]
    def password(
        self, create: bool, extracted: Sequence[Any], **kwargs: typing.Any
    ) -> None:
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
