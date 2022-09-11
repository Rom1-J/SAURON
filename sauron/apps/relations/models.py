import uuid

from django.db import models
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


# =============================================================================


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    note = models.TextField(blank=True)
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        User,
        related_name="tags",
        related_query_name="tags",
        on_delete=models.CASCADE,
    )

    relation = models.ForeignKey(
        Relation,
        related_name="tags",
        related_query_name="tags",
        on_delete=models.CASCADE,
    )


# =============================================================================


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    note = models.TextField(blank=True)
    attachment = models.FileField()

    relation = models.ForeignKey(
        Relation,
        related_name="attachments",
        related_query_name="attachments",
        on_delete=models.CASCADE,
    )


# =============================================================================


class Link(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    note = models.TextField(blank=True)
    link = models.URLField()

    relation = models.ForeignKey(
        Relation,
        related_name="links",
        related_query_name="links",
        on_delete=models.CASCADE,
    )
