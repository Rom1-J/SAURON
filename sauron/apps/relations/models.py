import uuid

from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import SafeString
from django.utils.translation import gettext_lazy as _

from sauron.apps.users.models import User


class Relation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    author = models.ForeignKey(
        User,
        related_name="relations",
        related_query_name="relations",
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    note = models.TextField(blank=True)

    relations = models.ManyToManyField("self", blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    attachments = models.ManyToManyField("Attachment", blank=True)
    links = models.ManyToManyField("Link", blank=True)
    nicknames = models.ManyToManyField("Nickname", blank=True)

    # =========================================================================

    def __str__(self) -> str:
        return f"{self.first_name.title()} {self.last_name.upper()}"


# =============================================================================


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    note = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#000000")

    author = models.ForeignKey(
        User,
        related_name="tags",
        related_query_name="tags",
        on_delete=models.CASCADE,
    )

    # =========================================================================

    @admin.display
    def colored_name(self) -> SafeString:
        return format_html(
            (
                "<div style='background: {}'>"
                "<span style='color: {}; filter: invert(1)'>{}</span>"
                "</div>"
            ),
            self.color,
            self.color,
            self.color,
        )

    # =========================================================================

    def uses(self) -> int:
        return -99

    # =========================================================================

    def __str__(self) -> str:
        return f"{self.name} ({self.color})"


# =============================================================================


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    note = models.TextField(blank=True)
    attachment = models.FileField()

    # =========================================================================

    def __str__(self) -> str:
        return f"{self.attachment.name} ({self.attachment.size})"


# =============================================================================


class Link(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    note = models.TextField(blank=True)
    link = models.URLField()

    # =========================================================================

    def __str__(self) -> str:
        return f"{self.link}"


# =============================================================================


class Nickname(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    note = models.TextField(blank=True)
    nickname = models.TextField(max_length=150, blank=True)

    # =========================================================================

    def __str__(self) -> str:
        return f"{self.nickname}"
