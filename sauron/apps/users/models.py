import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image

from sauron.utils.functions import PathAndRename


class User(AbstractUser):
    class Theme(models.TextChoices):
        DARK = "DK", _("Dark")
        LIGHT = "LT", _("Light")

    # =========================================================================

    id = models.UUIDField(
        _("Identification"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    theme = models.CharField(
        max_length=2, choices=Theme.choices, default=Theme.DARK
    )

    avatar = models.ImageField(
        upload_to=PathAndRename("users/avatar"), blank=True, null=True
    )

    # =========================================================================

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img = Image.open(self.avatar.path)

            if img.size > (128, 128):
                output_size = (128, 128)

                img.thumbnail(output_size)
                img.save(self.avatar.path)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"id": self.id})
