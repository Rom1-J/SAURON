from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Attachment, Link, Relation, Tag


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    class TagInline(admin.TabularInline):  # type: ignore[type-arg]
        model = Tag

    class AttachmentInline(admin.TabularInline):  # type: ignore[type-arg]
        model = Attachment

    class LinkInline(admin.TabularInline):  # type: ignore[type-arg]
        model = Link

    inlines = [TagInline, AttachmentInline, LinkInline]

    fieldsets = (
        (None, {"fields": ("author",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "relations",
                )
            },
        ),
        (_("Misc"), {"fields": ("note",)}),
    )
    list_display = [
        "author",
        "first_name",
        "last_name",
    ]
    search_fields = [
        "id",
        "author",
        "first_name",
        "last_name",
        "tags",
    ]


# =============================================================================
# =============================================================================


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "note",
                    "author",
                )
            },
        ),
    )
    list_display = [
        "name",
        "author",
    ]
    search_fields = [
        "id",
        "name",
        "author",
    ]


# =============================================================================
# =============================================================================


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "attachment",
                    "note",
                )
            },
        ),
    )
    list_display = [
        "attachment",
    ]
    search_fields = [
        "id",
        "attachment",
        "note",
    ]


# =============================================================================
# =============================================================================


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "link",
                    "note",
                )
            },
        ),
    )
    list_display = [
        "link",
    ]
    search_fields = [
        "id",
        "link",
        "note",
    ]
